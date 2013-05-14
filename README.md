# dreamer

a tool for creating visual hypertext stories


# current state of the project

I (JP) won't have time to work on this project for a while, probably the rest of 2013, so I'm writing up as much of the design in my head as possible so that other people can continue the work.  Please post any questions to the [the wiki](https://github.com/JPLeBreton/dreamer/wiki), I'm happy to answer and consult with anyone who is interested in helping.

Most of the material here is about user interface - my approach has been to design from the UI inward (towards the implementation), because accessibility is the highest single priority for a tool aimed at people who've never made games before.

The biggest missing puzzle piece is how best to make page elements dynamic.  Integrating the functionality of some Javascript library like jquery is the obvious choice; it's mature and does everything we'd need.  What subset of jquery's functionality is exposed, and how, is a major design question requiring much thought, hopefully by someone who knows that side of things better than myself.


# tenets and rationale

*Client-side creation application* -
I think Twine proliferated thanks in part to its being a piece of software you download once, install and use locally - it's not dependent on any server and works even if you don't have an internet connection.  Making Dreamer run in a web browser using HTML5-related technologies and supporting things like collaborative editing is appealing in some ways, but runs counter to this.  So a client application, written with a good cross-platform UI toolkit like Qt, seems like the best way to go and does not hinder us from using the web as our export format.

*Use proven web technologies* - HTML, CSS, and Javascript are the languages of the web.  Hypercard predated the web, but now that the web has been invented and matured, there is zero need to recapitulate it.  Dreamer stories export as web pages and are viewable in any web browser that can display images and run Javascript.

*Visual composition-based UI paradigm* - HTML allows you to create documents with nested elements, but this feature offers little more than potential confusion to someone who wants to make a visual hypertext story.  Because it's markup, text is a first-class citizen in HTML while images and other media are integrated by reference.  Photoshop's layers seem like a more appropriate UI model here, allowing users to place arbitrary images and fields of text on a page in a freeform composition.  This helps make the divergence in goals from Twine very clear.

*Support simple drawing tools* - This isn't as important and might be some real work, but I think people should be able to make something using only this app, not requiring any external art tools.  The art tools don't need to be any more advanced than MSPaint, so long as they let you sketch in color.  This helps even experienced artists who want to rough in all their page elements quickly.

*Iterative, community-driven development* - Dreamer must be open source so that no company can control or ruin it, as so often happens with game creation tools.  Dreamer would lend itself well to an iterative dev process in which feedback, particularly for the design of the creation UI, from people creating actual stories is taken into consideration.  The creation UI isn't a horribly complex app but the design I've outlined here will have rough edges and unanticipated pain points.  Listen to users, find what's not working well, and fix it.


# mockup

I created the following mockup to show what the creation application might look like editing an example story:

![Dreamer creation UI mockup](http://vectorpoem.com/etc/dreamer/dreamer_mockup1.png)


# concepts

*Story* - A story is the top-level document you author and export.  It consists of multiple *pages*, each of which contain *objects*.  The "source format" for a story file uses a .dr extension, while an exported story consists of a .html file (with its CSS and Javascript included in the HTML) and a directory containing non-text resources referenced in the HTML, such as images and sounds.  An entire story is presented visually in the creation UI as a node graph, exactly as in Twine's main view, in a "story view" dock/window not shown in the mockup above.

*Page* - A page is a single "place" within a *story*, containing multiple *objects*.  Pages in a story can be accessed nonlinearly by players, as in all hypertext, and by creators in the creation UI.  They're probably assigned a numeric order/value for convenience in things like "jump to page" in the creation UI.

*Object* - An object is an element within a *page*.  A single object can appear on multiple pages.  An object can hold text (with HTML formatting), an image link, an image drawn with the painting tools, or an embedded thing like video or audio.  Objects can be freely moved or resized on each page.  Every object has a property sheet in which their data can be edited.  Objects within a page 

*Script* - A script is a snippet of Javascript that can be associated with a *Story* (serving as a "global" script), a *Page*, or an *Object*.


## loose thoughts on objects, document structure

a single object can appear on multiple pages in multiple locations with multiple sizes.

(what's the same across pages, then?  text/image resources, link/script?  possible some concept like Unity's prefab vs instance is needed, though the complexity of inheritance is unecessary here)

objects are a user-facing concept, under the hood (ie on export) each usage of a object on a given page becomes its own unique div id.

in an object's properties you can see which pages it appears on

in a page's properties you can see which objects it "includes"

under the hood, pages keep lists of objects; export process walks this list to build DOM so objects that aren't used on any page are in the .dr file but not the exported story.

objects can have an image reference, ie an <img> element, but also painted raster data(?)  (if both, how are these integrated?  <img> vs CSS background?)


# development phases

Here are some rough milestone goals that could be used to development sets of related features.

## phase 1

* Creation UI can open, edit, save, and export basic stories.
* Pages comprised of objects:
** images (referenced, no paint UI yet)
** text
* Objects can be moved but not scaled.
* Click links to navigate between "pages" - no scripts yet.

## phase 2

* Story graph view, a la Twine.
* Scripts can be embedded in objects and do simple things, like control onhover and onclick behavior.
* Objects can be scaled on pages.

## phase 3

* Drawing tools support.
* Jquery features exposed to script so that Objects can be animated and change many properties at runtime.
* Start integrating early adopter feedback and prepare for 1.0 release.


## proposal for .dr document structure

* story name
* unordered list of pages
* unordered list of objects
* page:
 * page name
 * page script
 * page background color
 * page background image
 * page audio ambience
 * ordered list of page object instances (by name)
     - object instance position
     - object instance  size
     - object instance link (script or target)
     - object instance comment (not seen by player, used as img alt text)
* object:
 * object name
 * object text (can be blank)
 * object image ref (can be blank)
 * object image data (can be blank)
 * (all the following properties can be overridden on instances):
 * object position
 * object size
 * object link (script or target)


# export process

Build first: command line program for converting native format .dr files into html.  GUI app invokes the same code, as with Twine vs Twee.

An exported story looks like:

    [story directory]
     |
     +- [resource folder]
     |  |
     |  +- [local resources] image/audio/video files
     |  +- [cached folder] (if "offline" option used)
     |     |
     |     +- [cached resources] image/audio/video files
     |
     +- [this story].html
     +- [this story].css
     +- [this story].js
     +- [common scripts folder]
        |
    	+- dreamer.js
    	+- jquery.js (if "offline" option used)

"offline" export option fetches all remotely linked resources and caches them remotely, including jquery.  increases file size but you can play without a net connection.

include .css and .js inside .html for fewer files?

goal: make it pretty easy to host stories from public Dropbox folders, the way people do with Twine stories.


# dynamic object text

need some sort of special character/pattern to designate a substring in an object's text as referencing a user-defined variable, eg $NumberOfFruits, $PlayerName, whatever.  this should be recalculated as needed (maybe page script runs an "update page" function when anything happens, checks if any variables have changed and updates element content)
