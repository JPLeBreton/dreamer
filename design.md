
# ongoing design log

## layers (document structure)

a single layer can appear on multiple pages in multiple locations with multiple sizes.
(what's the same across pages, then?  text/image resources, link/script?  possible some concept like Unity's prefab vs instance is needed, though without inheritance)

layers are a user-facing concept, under the hood (ie on export) each usage of a layer on a given page becomes its own unique div id.

in a layer's properties you can see which pages it appears on
in a page's properties you can see which layers it features
under the hood, pages keep lists of layers; export process walks this list to build DOM so layers that aren't used on any page are in the .dr file but not the exported story.

layers can have an image reference, ie an <img> element, but also painted raster data(?)  (if both, how are these integrated?  <img> vs CSS background?)


## .dr document structure

* story name
* unordered list of pages
* unordered list of layers
* page:
 * page name
 * page script
 * page background color
 * page background image
 * page audio ambience
 * ordered list of page layer instances (by name)
    - layer instance position
    - layer instance  size
    - layer instance link (script or target)
    - layer instance comment (not seen by player, used as img alt text)
* layer:
 * layer name
 * layer text (can be blank)
 * layer image ref (can be blank)
 * layer image data (can be blank)
 * (all the following properties can be overridden on instances):
 * layer position
 * layer size
 * layer link (script or target)


## export process

command line program for converting native format .dr files into html, GUI app invokes the same code.

an exported story looks like:

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


## dynamic layer text

need some sort of special character/pattern to designate a substring in a layer's text as referencing a user-defined variable, eg $NumberOfFruits, $PlayerName, whatever.  this should be recalculated as needed (maybe page script runs an "update page" function when anything happens, checks if any variables have changed and updates element content)
