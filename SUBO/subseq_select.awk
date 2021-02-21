#!/bin/awk
# Fields: query id, subject id, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, BTOP
#	     $1		$2	    $3 		    $4		  $5	      $6	$7	 $8	  $9	   $10	  $11       $12     $13
BEGIN {FS = "\t"
       longest_length   = 41  # $4
       longest_begin    = 0   # $7
       longest_end      = 0   # $8
}
{
if (($4+0)<(longest_length+0) && ($4+0)>=32 && ($3+0)==100.00) {
	longest_length = $4
	longest_begin = $7
	longest_end = $8
	} # selects shortest substring with 100% match that is at least 32 nucleotides long
}
END { print longest_begin " " longest_end }
