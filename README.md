# Read_Relv
Minimal Read Mode for artiicle websites.

<p>So this is gonna be a new big project for me.<br>
Better version of my previous hardcoded Read Mode project.<p>

<p>Starting it...<br>
Added Basic file structure and added working basic starting flask implementation<br>
Made Simple form structure that passes the url to the backend.<p>

<p>The main thing starts now<br>
How to build the actual generalised algorithm<br>
I have decided a plan to go with<p>

<p>Firstly, Remove any clutter like ad divisions, sidebars, topbars, index etc.<br>
Removing clutter through keywords is a neccessary risk<br>
I need to find the balance so that it removes the clutter but not the main content<br>
So I observed some websites and found some divisions and keywords for obvious clutter<br><br>
Along with obvious tags like script and style, I will remove some clutter through keyword searching<br>
keywords like sidebar, feedback, subheader etc.<br>
<p>

<p>
Now, next step is finding candidates i.e. the containers or div that hold actual important content<br>
Now, comes the scoring part<br>
this is where I am gonna decide how much important the section is<br>
<p>

<p>
Now that I have made the basic core functionality,<br>
I have to primarily debug it and improve it by testing on various article websites<br>
then<br>
I have to format it and make it look better.<br>
<p>

<p>
While extracting and formatting the data I found an ineteresting bug,<br>
in this the content repeats multiple times, which I figured it out myself reason being that the find_all fetches and brings the nested text each time it spots the searches I put in the blocks list.<br>
To solve it I can simply make a seen named container which checks if the content is already been there or not.<br>
<br>
Now that I almost fixed extraction part the whole content is coming in a single line, now gotta figure out the reason behind it.<br>
I get it why it failed working, the thing is that I am fetching the parent and child content in such a way it breaks my if else formatting logic in the extractContent function as I have already fetched the blocks in the parent so it ignores it when the code comes to the actual block to prevent duplication<br>
Its the troubling part of nested nested divisions and content.<br>
Still finding out a way to fix it<br>
<p>