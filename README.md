<h1>Python Console Chat</h1>
<h3>Intro</h3>
<p>Welcome to the Chatting with Python course! Here we will briefly learn how to develop a basic chat application in the console.</p>
<h3>Steps to reproduce this</h3>
<p>Please feel free to refer to the code in the example I've laid out for you above. Do your best to do it on your own and figure out how to create your own functions and variables, following the steps written below.</p>
<ol>
    <li>Build your dictionary. Specifically choose which key, value pairings you wish to use (i.e. what you want to ask the console and what you want it to say back)</li>
    <li>Make a joke dictionary nested within your overall dictionary when someone writes "tell me a joke" to the console.</li>
    <li>Create a function that randomly selects a joke from that nested joke dictionary so it seems as if the console is randomly telling a joke.</li>
    <li>Create a function that will call each of these key, value pairings upon command. Within this function, use a <code>while</code> loop to develop the illusion of the computer constantly asking you to write back to it. This will be useful in allowing the user to constantly keep talking with the console.</li>
    <li>Within that <code>while</code> loop, make sure to add conditional statements that exit the loop when typing a certain command (like "goodbye"). Within these commands, feel free to call your key, value pairings as you wish.</li>
</ol>
<h3>How it works</h3>
<p>Run the Python file. Once it loads, it should pull up a console queue that asks you to talk to it. Using the key, value responses from the dictionary you had created earlier, simply write out the keys (i.e. "hello", "how are you", etc) and watch it respond.</p>