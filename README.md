# TT_rework_Tech
Miscellaneous scripts for TT submition

## executing the replacement of technology
The python script needs two parameters, the directory where it will find the .mag files to replace and a flag, when set to true it replaces the node to 130A, when set to false it replaces the node to 130B
```shell
python3 replace_120A.py xschem/skywater_submission/ --flag False 
```

## Customizing the TCL file for mos generation with spice file
Magic uses Tcl scripts to define how transistors are created. The script that governs device generation is found at $PDK_ROOT/sky130B/libs.tech/magic/sky130B.tcl. At around line 4910 (more less) you will find this text, this is where the Tcl file has the definitions for the generation of CMOS geometries based on spice files, is in here the modifications are done as it can be seed in the following  part
```shell
#----------------------------------------------------------------
# MOS defaults:
#----------------------------------------------------------------
#    w       = Gate width
#    l       = Gate length
#    m	     = Multiplier
#    nf	     = Number of fingers
#    diffcov = Diffusion contact coverage
#    polycov = Poly contact coverage
#    topc    = Top gate contact
#    botc    = Bottom gate contact
#    guard   = Guard ring
#
# (not user-editable)
#
#    lmin    = Gate minimum length
#    wmin    = Gate minimum width
#----------------------------------------------------------------

#----------------------------------------------------------------
# pmos: Specify all user-editable default values and those
# needed by mos_check
#----------------------------------------------------------------
```

```shell
proc sky130::sky130_fd_pr__pfet_01v8_defaults {} {
    return {w 0.42 l 0.15 m 1 nf 1 diffcov 100 polycov 100 \
		guard 1 glc 0 grc 0 gtc 0 gbc 1 tbcov 100 rlcov 100 \
		topc 1 botc 1 poverlap 0 doverlap 1 lmin 0.15 wmin 0.42 \
		compatible {sky130_fd_pr__pfet_01v8 \
		sky130_fd_pr__pfet_01v8_lvt sky130_fd_pr__pfet_01v8_hvt \
		sky130_fd_pr__pfet_g5v0d10v5} full_metal 1 \
		viasrc 100 viadrn 80 viagate 100 \
		viagb 0 viagr 0 viagl 0 viagt 0}
}
```
- glc is refered to the left guard ring (a value of 1 represents that a vias will be placed on this position and a value of 0 represents the absence of it)
- grc is refered to the right guard ring
- gtc is refernd to the top guard ring
- viadrn is references to the vias dufission on drain
- viasrc is references to the vias dufission on source

### modifications or replacement

The tcl file on this repo cotains he modifications for the nmos and pmos of 1v8, you can either download it and replace on the folder or modify it at your convenience using the info provided above, good luck
