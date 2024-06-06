
set current_dir [pwd]

set resid 3113

set numframes [molinfo top get numframes]

set outfile [open "$current_dir/residue_trajectory.txt" w]

for {set i 0} {$i < $numframes} {incr i} {
    set sel [atomselect top "resid $resid" frame $i]
    set com [measure center $sel]
    puts $outfile "$i $com"
    $sel delete
}

close $outfile