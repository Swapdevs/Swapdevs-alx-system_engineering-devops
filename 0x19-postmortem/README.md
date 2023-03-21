# 0x19-postmortem

https://ibb.co/TKSK4Rq

# Summary
23th Oct. 2021 From 3:45 PM to 4:12 PM UTC+1 all requests for the homepage to our web server got a 503 Service Unavailable.
# Timeline
- 3:46 PM: Refresh the page
- 3:49 PM: Engaged the both front end and backend teams
- 3:41 PM: Rollback changed successfully
- 3:43 PM: Restart the server
- 3:45 PM: 100% of traffic back online
- 3:52 PM: Start debugging the push with the problem
- 4:06 PM: Bugs fixed and pushed the changes
- 4: 07 PM: Restart the server
- 4: 11 PM: 100% traffic back online with the new updates
- 4:12 PM: Refresh the page
# Root cause and resolution

We can see that the URL is reserved. The "" sign means any host header, and the :80 means anything on port 80. Since there is no application path after the final "/" it reserves anything that runs on port 80. This is what is causing the 503 Service Unavailable errors, as this reservation will prevent W3SVC from obtaining the rights to listen on port 80 when it tries to start the site. Furthermore, applications that run in IIS do not need explicit reservations to run, only non-IIS applications have to reserve a URL namespace if they want to use HTTP to listen for requests.  One example are WCF applications that are running on HTTP, as these are non-IIS applications that use HTTP to listen for requests.   To resolve the problem for the default web site, we have to remove the reserved namespace for port 80 with the following command.

netsh http delete urlacl http://+:80/

URL reservation successfully deleted


After removing this namespace, WCF applications or other non-IIS applications running on this server may break.  So a new URL reservation may be needed for those applications.  The new URL reservation should point to the specific application on port 80, not the root.  This will prevent the URL reservation from blocking all applications under port 80.  The next question is who added the namespace in the first place?  There is no real way to identify that, however the HTTPEvent 15007 in the System Event log will give a good indication of the Date and Time the reservation was made.

# Corrective and preventative measures
To prevent similar problems from happening again we will 
- We deployed a monitoring software to our servers which will be monitoring the website and one of the software are Network Traffic requests and responses and configure it to make an alert to the developer teams for quick resolution.
