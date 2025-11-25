

## A Blog About GitHub Issues using a PAT ##

---

### Navigating and Using the PAT is an effort ###

---

I was working on a python project to create a simple program for a user to particapate.  The intent was to review my skills using vs code with git (bash terminal) and github.

I started my project in git and VS code.  I created a new directory and added a python file.  Since I chose the VS/git order I didn't create a README.md (markdown) until later.

Next I moved over to github and created a new repository.
I haven't been using github much.  When I used the drop down menu under my user icon, than selected Accessibility (right side of github page), and then Developer Settings (left side of github page), I clicked on the key emoji and Personal access tokens.  
I noticed there are now two options for the PAT:

1) fine-grained tokens (new)
2) Tokens (classic - the original)

I opted to generate the new fine-grained token.  And, ofcourse, copied the new token to save and use again.
The problem(s) came when I attempted to use git to add and commit my vs code (local repository) to github (remote repository).

I was unsuccessful and received numerous errors:
1). 403
2). permission denied
3). user not recognized
4). and some others !!!

And here is why it's good to build programs, and do projects, and use a text editor (vs code, sublime, Atom, whatever) with git and github. 

ERROR HANDLING

Dealing with errors is a constant when writing code. 
In this instance it was understanding the software and how I needed to interact with it. 
That being said, even with the new little github helper, I needed to search for a while before I found a solution.
I tried to use Google, and looked at a few youTube videos but that didn't solve my problem.
So I went back to look at the PAT page.
After clicking on and generating a new fine-grained token there is more to do.
Navigate down the page to permissions to tell github you have permission to push to all, or one of your repositories.

So now I have a better understanding of this new process.

💡