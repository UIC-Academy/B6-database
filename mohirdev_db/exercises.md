## 1. Simple SELECT (20 exercises)

Use `select`, `where`, `order_by`, `limit`, `offset`, `label`, boolean filters.

1. Select all active users ordered by `created_at` descending.
2. Select `first_name`, `last_name`, and `phone` of users from a specific `country_id`.
3. Select the 10 newest courses that are published.
4. Select lessons with `max_attempts_count > 3`, ordered by `lesson_order`.
5. Select users who are staff but not superusers.
6. Select course names and reward stars, ordered by stars descending.
7. Select lessons with type `"video"` and `is_active = true`.
8. Select notifications sent to all users (`is_send_to_all = true`).
9. Select modules of a given course ordered by `course_order`.
10. Select users where `last_login` is NULL.
11. Select lesson names with their current rating, label rating as `rating`.
12. Select courses that are inactive or unpublished.
13. Select users older than 25 ordered by age ascending.
14. Select lesson questions created after a given date.
15. Select lesson resources with non-null captions.
16. Select top 5 highest-rated lessons.
17. Select users with deleted flag set to false.
18. Select courses filtered by `category_id`.
19. Select authors with more than 5 years of experience.
20. Select lessons where `attempt_interval` is not NULL.

---

## 2. Aggregate Functions (NO GROUP BY) — 10 exercises

Only scalar aggregates.

1. Count total users.
2. Count active courses.
3. Get maximum lesson rating.
4. Get minimum user age.
5. Get average lesson rating.
6. Count total enrollments.
7. Count lessons with type `"quiz"`.
8. Get average reward stars across all courses.
9. Count deleted users.
10. Get latest lesson creation timestamp.

---

## 3. GROUP BY + HAVING (15 exercises)

1. Count courses per category.
2. Count lessons per module.
3. Count enrollments per course.
4. Average lesson rating per course.
5. Count lessons per author.
6. Count users per country.
7. Count lessons per type, only types with more than 5 lessons.
8. Average user age per region, only regions with avg age > 30.
9. Count ratings per lesson, only lessons with more than 3 ratings.
10. Count modules per course having more than 2 modules.
11. Count lesson questions per lesson.
12. Count certificates per user having more than 1 certificate.
13. Average rating per lesson type.
14. Count enrollments per user having at least 2 enrollments.
15. Count lessons per course ordered by lesson count descending.

---

## 4. Joins (2 tables) — 20 exercises

1. Join users with enrollments, select user name and course id.
2. Join courses with authors.
3. Join lessons with modules.
4. Join modules with courses.
5. Join lesson resources with media.
6. Join lesson rates with users.
7. Join courses with categories.
8. Join course tags with tags.
9. Join user certificates with courses.
10. Join enrollments with users.
11. Join enrollments with courses.
12. Join lessons with lesson questions.
13. Join lessons with lesson answers.
14. Join notifications with users.
15. Join courses with banners (media).
16. Join users with avatars (media).
17. Join lessons with videos (media).
18. Join lesson homework attempts with users.
19. Join lesson homework attempts with lessons.
20. Join user education with education.

---

## 5. Complex Joins (3+ tables) — 10 exercises

1. Users → Enrollments → Courses: list user name and course name.
2. Courses → Modules → Lessons: list course name and lesson name.
3. Lessons → LessonRate → Users: list lesson name and rater name.
4. Courses → CourseTag → Tag: list course name and tag name.
5. Users → UserCertificate → Courses: list user and certified course.
6. Courses → Modules → Lessons → LessonResource: list lesson and resource file.
7. Lessons → LessonQuestion → LessonAnswer → Users: list question text and answer author.
8. Courses → Author → Media: list course name and author avatar URL.
9. Users → Enrollments → Courses → Category: list user and course category.
10. Lessons → LessonHomeworkAttempt → Media → Users: list lesson name, submitted file, and user.

