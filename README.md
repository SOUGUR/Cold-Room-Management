The Cold Room Management System is a Django-based web application designed to efficiently manage and monitor inventory stored in a cold room environment. 
This project was developed in a collaborative approach to solving real-world problems in inventory management in Biocon Biologics.

Key Features:
1. Material Addition and Tracking:

2. Expiry Date Management: Add materials with specific expiry dates, automatically track them, and receive notifications as they near expiry.
3. Batch Management: Supports batch tracking of materials, ensuring that each batch's expiry is monitored independently.

4. Real-Time Updates: View a dynamic list of all materials in the inventory, including details such as quantity, expiry dates, and storage conditions.
5. Sorting and Filtering: Easily sort and filter materials based on expiry date, material type, or other custom criteria.
Upcoming Expiry Alerts:

6. Automated Alerts: Automatically generate a list of materials that are approaching their expiry date, helping users make informed decisions about usage or disposal.
7. Email Notifications: Integrates with email services to send alerts to responsible personnel about upcoming expiries, ensuring timely action.
8. User Authentication and Role-Based Access Control.

9. Secure Login: Implements user authentication to ensure that only authorized personnel can access the system.
10. Role-Based Permissions: Different roles (e.g., manager, staff) have varying levels of access to features, ensuring a secure and organized workflow.

Technologies Used:
1. Django Framework: The backbone of the application, providing a robust and scalable framework for managing the application's backend, including models, views, and templates.
2. SQLite Database: Used for managing the data related to inventory, users, and expiry dates, offering a lightweight and efficient solution.
3. HTML/CSS: Utilized for creating a responsive and user-friendly interface, ensuring ease of use across different devices.
4. Django-Crontab: Integrated for scheduling tasks like sending expiry notifications, allowing the system to operate smoothly without manual intervention.
5. Python: Core logic, including inventory management, expiry tracking, and user authentication, is implemented in Python, showcasing proficiency in backend development.
