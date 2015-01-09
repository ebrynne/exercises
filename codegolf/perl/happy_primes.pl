# Read one positive integer from stdin, then output 'happy' or 'sad' and then 'prime' or 'non-prime' depending on
# whether the number is 'happy' and 'prime' or not. For this problem a 'happy' number is a number if, by repeating the
# process of squaring each of the digits of the number and then summing the results to get a new value, eventually a 
# value of 1 can be reached. All non-happy numbers will eventually enter a loop.
# This solution: 183 characters
$n=$p=<>;%h={};while(!$h{$n}){$h{$n}=1;$n=eval join'+',map{$_*$_}split(//,$n)};if($n==1){$s='happy '}else{$s='sad '};@a=map{$p%$_}(2..$p-1);if(0~~@a&&$p-1){$s.='non '};print$s.'prime'