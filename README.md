Within our team our development process is as follows:

New features/fixes/Reworkings (Stories) are outlined in our Project backlog within this repository.  When a Backlog task is selected, it is then made into an issue report and assigned to a developer on the team and moved into the In Progress section of the project..

The developer will then work on the task and implement changes within their workspace branch until they feel confident in the functionality and the implementation, at which point they will merge it into their personal testspace.  Upon reaching the testspace a Pull Request is created to move from that individual testspace into our joint testspace, other developers can safely access that testspace branch to do any necessary testing as well as leave necessary feedback, request changes, or approve the move into our joint testing branch.  This is also the point at which the story will be considered to be in peer review an be moved into Dev Complete upon approval into the Joint Testing Space.

When we as a team reach a solid development point within our joint testing branch, a Pull Request will be made from Joint Testing into our main branch.  This is the sort of point where we feel comfortable to require all developers to update their local work and testspaces with the master if such is approved.  In order for it to be approved, approval and code review is required from all active developers.

After a new master branch is established the Story will be considered complete and move into its resting place of In Main.  The process continues until the master branch reaches the point of being a sufficient product in relation to the outlined product requirements.

Process Author: John P Armentor
#email:     johnparmentor@gmail.com
#Date:      2020 02 17
