# m3usplitter
<p>I was annoyed by a number of irrelevant channels delivered in the standard playlist (m3u). Too much in languages I don't understand. My TV was dying after 4MB playlist upload (SIPTV). Some groups are so big, it took me half an hour to reach something starting with K with my TV remote. Every time I was refreshing my program list, I had to strip German, French, Arab etc. Even using atom and regexp it was a pain. Ofc it is nothing wrong with it, I like it. Just a lot of recurring work. So finally I have decided to write a script to simplify the task of striping.</p>
<p>So here you have simple python script allowing you to select channel groups and even to split large groups to alphabetized smaller groups.</p>
<p>You need python3 installed. On Windows and macOS you will need to install it first.</p>
<p>Script works from command line. The easiest way is to put it in the same directory/folder as your original playlist. Then invoke a command line/terminal and run following command:</p>
<p><code>python3 m3usplit.py -i <name of your original playlist> -o <name of your desired new playlist></code></p>
<p>There are two additional (not mandatory) options.</p>
<p><code>-s xxxx</code></p>
<p>where you can specify the number of items in a group that will trigger alphabetizing this group. After alphabetization instead of one huge "VOD" group you will have VOD A, VOD B, VOD C groups containing programs starting with a particular alphabet character.</p>
<p>Code:</p>
<p><code>-a</code></p>
<p>which instructs the script to skip overwriting output file (e.g when you forget to select an interesting group, but don't want to repeat the rest of the selection process).</p>
<p>After invoking the script you will have a chance to select groups from the input file. You need to press 'y' everytime you want a particular group to be included in the output file.</p>
<p>To skip group you press enter.</p>
<p>That's all, enjoy. And don't forget to report any problems.</p>
