from datetime import datetime

from sqlalchemy import (
    String,
    BigInteger,
    Boolean,
    ForeignKey,
    DateTime,
    func,
    SmallInteger,
    JSON,
    Integer,
    Text,
    Float,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import BaseT


class Base(BaseT):
    __abstract__ = True
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )


class User(Base):
    __tablename__ = "users"

    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    avatar_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="SET NULL"), nullable=True
    )
    bio: Mapped[str] = mapped_column(String(255), nullable=True)
    age: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    gender: Mapped[str] = mapped_column(String(6), nullable=True)
    country_id: Mapped[str] = mapped_column(
        BigInteger, ForeignKey("countries.id", ondelete="CASCADE"), nullable=True
    )
    region_id: Mapped[str] = mapped_column(
        BigInteger, ForeignKey("regions.id", ondelete="CASCADE"), nullable=True
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    last_login: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    
    avatar: Mapped["Media"] = relationship("Media", back_populates="user")
    country: Mapped["Country"] = relationship("Country", back_populates="users")
    region: Mapped["Region"] = relationship("Region", back_populates="users")
    experiences: Mapped[list["UserExperience"]] = relationship(
        "UserExperience", back_populates="user"
    )
    educations: Mapped[list["UserEducation"]] = relationship(
        "UserEducation", back_populates="user"
    )
    certificates: Mapped[list["UserCertificate"]] = relationship(
        "UserCertificate", back_populates="user"
    )

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User(phone={self.phone})"


class UserExperience(Base):
    __tablename__ = "user_experiences"

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String(100))
    position: Mapped[str] = mapped_column(String(100))
    website_url: Mapped[str] = mapped_column(String(100))
    skills: Mapped[dict] = mapped_column(JSON, nullable=True)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    user: Mapped["User"] = relationship("User", back_populates="experiences")

    def __repr__(self):
        return f"UserExperience(user_id={self.user_id})"


class UserEducation(Base):
    __tablename__ = "user_educations"

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    education_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("educations.id", ondelete="CASCADE")
    )
    field: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    user: Mapped["User"] = relationship("User", back_populates="educations")

    def __repr__(self):
        return f"UserEducation(user_id={self.user_id})"


class Education(Base):
    __tablename__ = "educations"

    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(20))
    website_url: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"Education(name={self.name})"


class UserCertificate(Base):
    __tablename__ = "user_certificates"

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    course_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("courses.id", ondelete="CASCADE")
    )
    attachment_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String(100))
    
    user: Mapped["User"] = relationship("User", back_populates="certificates")
    course: Mapped["Course"] = relationship("Course", back_populates="certificates")
    attachment: Mapped["Media"] = relationship("Media", back_populates="certificates")

    def __repr__(self):
        return f"UserCertificate(user_id={self.user_id})"


class Course(Base):
    __tablename__ = "courses"

    author_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("authors.id", ondelete="CASCADE")
    )
    banner_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))
    category_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("categories.id", ondelete="CASCADE")
    )
    reward_stars: Mapped[int] = mapped_column(Integer)
    is_published: Mapped[bool] = mapped_column(Boolean, default=False)
    
    author: Mapped["Author"] = relationship("Author", back_populates="courses")
    banner: Mapped["Media"] = relationship("Media", back_populates="courses")
    category: Mapped["Category"] = relationship("Category", back_populates="courses")
    certificates: Mapped[list["UserCertificate"]] = relationship(
        "UserCertificate", back_populates="course"
    )
    # 1
    # tags: Mapped[list["Tag"]] = relationship(
    #     "Tag", secondary="course_tags", back_populates="courses"
    # )
    # 2
    tags: Mapped[list["CourseTag"]] = relationship(
        "CourseTag", back_populates="course"
    )

    def __repr__(self):
        return f"Course(name={self.name})"


class Author(Base):
    __tablename__ = "authors"

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    avatar_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="CASCADE"), nullable=True
    )
    experience_years: Mapped[int] = mapped_column(SmallInteger)
    
    courses: Mapped[list["Course"]] = relationship("Course", back_populates="author")
    avatar: Mapped["Media"] = relationship("Media", back_populates="authors")

    def __repr__(self):
        return f"Author(first_name={self.first_name})"


class CourseTag(BaseT):
    __tablename__ = "course_tags"
    """
    Intermediary Table | Association table
    """

    course_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True
    )
    
    course: Mapped["Course"] = relationship("Course", back_populates="tags")
    tag: Mapped["Tag"] = relationship("Tag", back_populates="courses")

    def __repr__(self):
        return f"CourseTag(course_id={self.course_id})"


class Enrollment(Base):
    __tablename__ = "enrollments"

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    course_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("courses.id", ondelete="CASCADE")
    )
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"Enrollment(user_id={self.user_id})"


class Module(Base):
    __tablename__ = "modules"

    course_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("courses.id", ondelete="CASCADE")
    )
    name: Mapped[str] = mapped_column(String(100))
    sort_order: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"Module(course_id={self.course_id})"


class Lesson(Base):
    __tablename__ = "lessons"
    
    module_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("modules.id", ondelete="CASCADE")
    )
    video_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="CASCADE"), nullable=True
    )
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    current_rating: Mapped[float] = mapped_column(Float)
    type: Mapped[str] = mapped_column(String(20))
    max_attempt_count: Mapped[int] = mapped_column(Integer)
    attempt_interval_hours: Mapped[int] = mapped_column(Integer)
    sort_order: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"Lesson(module_id={self.module_id})"


class LessonQuestion(Base):
    __tablename__ = "lesson_questions"

    lesson_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("lessons.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    text: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"LessonQuestion(lesson_id={self.lesson_id})"


class LessonResource(Base):
    __tablename__ = "lesson_resources"

    lesson_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("lessons.id", ondelete="CASCADE")
    )
    resource_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="CASCADE")
    )
    caption: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"LessonResource(lesson_id={self.lesson_id})"


class LessonRate(Base):
    __tablename__ = "lesson_rates"

    lesson_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("lessons.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    star_count: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"LessonRate(lesson_id={self.lesson_id})"


class LessonAnswer(Base):
    __tablename__ = "lesson_answers"
    
    lesson_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("lessons.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    question_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("lesson_questions.id", ondelete="CASCADE")
    )
    text: Mapped[str] = mapped_column(String(100))
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f"LessonAnswer(lesson_id={self.lesson_id})"


class UserHomeworkAttempt(Base):
    __tablename__ = "user_homework_attempts"

    lesson_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("lessons.id", ondelete="CASCADE")
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE")
    )
    workfile_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="CASCADE")
    )
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"UserHomeworkAttempt(lesson_id={self.lesson_id})"


class Notification(Base):
    __tablename__ = "notifications"

    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=True
    )
    course_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("courses.id", ondelete="CASCADE"), nullable=True
    )
    module_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("modules.id", ondelete="CASCADE"), nullable=True
    )
    category_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("categories.id", ondelete="CASCADE"), nullable=True
    )
    title: Mapped[str] = mapped_column(String(100))
    message: Mapped[str] = mapped_column(String(100))
    is_sent_to_all: Mapped[bool] = mapped_column(Boolean, default=False)
    image_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("media.id", ondelete="CASCADE"), nullable=True
    )

    def __repr__(self):
        return f"Notification(user_id={self.user_id})"


# ============================ COMMON


class Media(Base):
    __tablename__ = "media"

    file: Mapped[str] = mapped_column(String(100), nullable=True)
    
    user: Mapped["User"] = relationship("User", back_populates="avatar")
    certificates: Mapped[list["UserCertificate"]] = relationship(
        "UserCertificate", back_populates="media"
    )
    authors: Mapped[list["Author"]] = relationship("Author", back_populates="avatar")
    courses: Mapped[list["Course"]] = relationship("Course", back_populates="banner")

    def __repr__(self):
        return f"Media(user_id={self.user_id})"


class Country(BaseT):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    code: Mapped[str] = mapped_column(String(100), nullable=True)
    
    users: Mapped[list["User"]] = relationship("User", back_populates="country")
    regions: Mapped[list["Region"]] = relationship("Region", back_populates="country")

    def __repr__(self):
        return f"Country(id={self.id})"


class Region(BaseT):
    __tablename__ = "regions"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    country_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("countries.id", ondelete="CASCADE")
    )
    
    users: Mapped[list["User"]] = relationship("User", back_populates="region")
    country: Mapped["Country"] = relationship("Country", back_populates="regions")

    def __repr__(self):
        return f"Region(id={self.id})"


class Category(BaseT):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    
    courses: Mapped[list["Course"]] = relationship("Course", back_populates="category")

    def __repr__(self):
        return f"Category(id={self.id})"


class Tag(BaseT):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    
    courses: Mapped[list["CourseTag"]] = relationship("Course", back_populates="tags")

    def __repr__(self):
        return f"Tag(id={self.id})"
