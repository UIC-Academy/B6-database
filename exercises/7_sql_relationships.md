# SQL Relationships

### 1. **Author → Book**
An author can write multiple books, but each book is written by one author.

### 2. **Customer → Order → Product**
A customer places multiple orders, each order can include multiple products. Products can appear in many orders.

### 3. **Teacher → Class → Student**
Each class is taught by one teacher. Each class has multiple students. A student can enroll in multiple classes.

### 4. **User → Post → Comment**
A user can create posts. Posts can have multiple comments. Each comment is written by a user.

### 5. **Doctor → Appointment → Patient**
Each appointment is between one doctor and one patient. A doctor can have many appointments. A patient can have appointments with different doctors.

### 6. **Company → Department → Employee**
Each company has multiple departments. Each department employs multiple people, but belongs to one company.

### 7. **Vendor → Product → OrderItem**
Vendors provide products. Products are sold through order items. Each order item refers to a product.

### 8. **Project → Task → Employee**
Projects contain tasks. Tasks are assigned to employees. Each task belongs to one project and is assigned to one employee.

### 9. **University → Faculty → ResearchPaper**
Each university has multiple faculties. Each research paper is published by a faculty member belonging to a university.

### 10. **Warehouse → Shipment → InventoryItem**
A warehouse sends out shipments. Each shipment includes multiple inventory items. Each inventory item can be in multiple shipments.