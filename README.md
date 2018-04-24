# snapshotPruner
Snapshot Pruner
<html>

<h1>Rules</h1>

<ul>
	<li>Implementation must be compliant with either Python 2.7+ or Python 3.6+</li>
	<li>Use only standard libraries, no external libraries</li>
	<li>You should review the <a href="https://docs.python.org/3/library/datetime.html">datetime</a> module before starting</li>
	<li>Use the editor or IDE of your choice</li>
	<li>Use any outside resource (books, message boards, Stack Overflow, etc.)</li>
	<li>If you pull in code from somewhere else, cite your sources</li>
	<li>If you need to make any assumptions, document them in the code</li>
</ul>

         
<h1>The Problem</h1>

<p>Every night, an automated process captures a snapshot of a database and uploads that snapshot to a persistent data store. These snapshots are very large and to reduce our storage costs we want to prune some of them.</p>

<h1>Objective</h1>

<p>Implement a function that will be used to determine which snapshots can be pruned. The function will <strong>receive a single parameter</strong> that is a list of snapshots, and is expected to <strong>return a list of snapshot IDs</strong> that can be pruned.</p>

<p>For example, the function might be called like this:</p>

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><code>snapshot_ids_to_prune = your_function(snapshots)</code></div>

<p><br>
<strong>snapshots</strong>&nbsp;is a list of tuples.&nbsp;Each tuple has three items: a snapshot ID, the UTC created date, and the status. The status can either be "available" or some other string. Example input:</p>

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
<code>[<br>
&nbsp; ('beta-1', datetime(2017, 10, 1, 14, 10, 30), 'available'),<br>
&nbsp; ('beta-2', datetime(2018, 1, 20, 18, 1, 34), 'available'),<br>
&nbsp; ('beta-3', datetime(2018, 1, 22, 8, 45, 22), 'pending'),<br>
&nbsp; ('beta-1-final', datetime(2018, 1, 18, 12, 42, 37), 'available'),<br>
&nbsp; ('live-1-final', datetime(2017, 10, 16, 3, 56, 32), 'available'),<br>
&nbsp; ('live-2-final', datetime(2017, 12, 12, 10, 23, 34), 'available'),<br>
&nbsp; ('live-seed-1', datetime(2017, 10, 2, 11, 9, 29), 'available'),<br>
&nbsp; ('live-seed-2', datetime(2017, 10, 17, 11, 10, 25), 'available'),<br>
&nbsp; ('live-seed-3', datetime(2017, 11, 2, 11, 8, 44), 'available'),<br>
&nbsp; ('live-seed-4', datetime(2017, 11, 17, 11, 11, 47), 'available'),<br>
]</code></div>

<p><br>
The problem is divided into 3 distinct phases. Each phase builds onto the logic of the previous phases. To get full credit, you need to submit a solution for each phase.&nbsp;</p>

<hr>
<h1>Phase 1</h1>

<p>Return all snapshot IDs for only the snapshots that have a status of "available" and the ID starts with "beta" or "test" regardless of when the snapshot was created.</p>

<h2>Example output</h2>

<p>Assuming the current month is January 2018 and using the example input above, the expected return value would be:</p>

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><code>beta-1, beta-2, beta-1-final</code></div>

<hr>
<h1>Phase 2</h1>

<p>Return all snapshot IDs for only the snapshots that have a status of "available" and:</p>

<ul>
	<li>Match any snapshots detected from Phase 1,</li>
	<li>ID starts with "live" and ends with "final" and was not created during the current month, the previous month, or the month before. If the current month is January, you only want to return snapshots created before November.</li>
</ul>

<h2>Example output</h2>

<p>Assuming the current month is January 2018 and using the example input above, the expected return value would be:</p>

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><code>beta-1, beta-2, beta-1-final, live-1-final</code></div>

<hr>
<h1>Phase 3</h1>

<p>Return all snapshot IDs for only the snapshots that have a status of "available" and:</p>

<ul>
	<li>Match any snapshots detected from Phase 2,</li>
	<li>ID starts with "live-seed", was not created during the current month, the previous month, or the month before, and is not the first snapshot of the month. If the current month is January, you only want to return snapshots created before November if they are not the first snapshot of the month.</li>
</ul>

<h2>Example output</h2>

<p>Assuming the current month is January 2018 and using the example input above, the expected return value would be:</p>

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px"><code>beta-1, beta-2, beta-1-final, live-1-final, live-seed-2</code></div>

<p>&nbsp;</p>

    
    

</body></html>
