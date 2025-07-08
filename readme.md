# Reflow!

It's a YSWS. You ship something, we ship something to you in return. Run by gh@pmnlla

## Phase 1: Submit a design!

**You ship:** A printed circuit board.

- Your full design criteria is situated at [the website](https://reflow.hackclub.com). Have a look through it, you'll need it later :3
- Your folder structure should look just about like this:
```   
    - pcb                          
       └──name of your pcb                                                                                    
         ├────────README.md                                                 
         └────────cad                                                   
                   ├──────<name>.kicad_sch                              
                   ├──────<name>.kicad_pcb                             
                   ├──────<name>.kicad_dru                          
                   └──────<name>.kicad_pro     
                                               
                                               
```
  Send it over in a PR, we'll review it, and dispatch the WS prize!
- A series of files you are not allowed to upload:
  - Anything with wildcards, relative paths, or attempts to escape your submission in the /pcb directory
  - PCB files that do NOT pass DRC with 0 errors.
  - Edits to folders you have not made the previous commit to, i.e. folders that are not your PCB.
  - Backups, ZIPs, or entire component libraries. There should be a link to where to find them in your README.
  - Gerbers - unlike onboard, this YSWS generates gerbers per every submission, for manual reviewl You do not need to upload them, and it is discouraged.

Got questions? You can reach me on slack @ `U078HNSV750`

**We ship:** A practice kit to learn SMD soldering with!

You'll get a:
- Practice board, with a set functionality of a 7 segment counter. 4 of them, to be exact.
- Components to populate at least one of the boards with
- A pair of tweezers
- A tub of flux
- A tin of solder paste, low melt, unleaded.
- A USB-C powered hotplate!

## Phase 2: Learn to solder:

**You ship:** Evidence of a completed and functional practice board, to the smallest components you can see and solder.
**We ship:** Funds, through HCB, for you to get your very own design made, and get the parts to assemble it with!
