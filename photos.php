<?php include("header.php"); ?>
<h1>Photo Gallery</h1>
<p>Throughout the years we have amassed quite a number of photos documenting our grand exploits, achievements, and fun, both on and off the fencing piste. Here we present to you a selection of these pictures, all taken by members of the good ol' Flaming Blades.</p>
    <h2>CHAMPS 2010</h2>
    <ul class="photos">
    <?php
					$imgs = glob("photos/champs2010/*.*");
					$thumbs = glob("photos/champs2010/thumbs/*.*");
					for ($i=0; $i<count($imgs); $i++) {
					$img = $imgs[$i];
					$thumb = $thumbs[$i];
					echo '<li><a href="'.$img.'" rel="lightbox[champs2010]" title="2010 Midwest Fencing Conference Championships, University of Notre Dame, 6-7 Mar"><img src="'.$thumb.'"></a></li>'; } ?>
	</ul>
    
    <h2>STABBED IN THE HEART 2010</h2>
    <ul class="photos">
    <?php
					$imgs = glob("photos/stabbed2010/*.*");
					$thumbs = glob("photos/stabbed2010/thumbs/*.*");
					for ($i=0; $i<count($imgs); $i++) {
					$img = $imgs[$i];
					$thumb = $thumbs[$i];
					echo '<li><a href="'.$img.'" rel="lightbox[stabbed2010]" title="Stabbed In The Heart (USFA), 21 Feb 2010, Oberlin College"><img src="'.$thumb.'"></a></li>'; } ?>
    </ul>
    <h2>OSUS 2009</h2>
    <ul class="photos">
    <?php
					$imgs = glob("photos/osu2009/*.*");
					$thumbs = glob("photos/osu2009/thumbs/*.*");
					for ($i=0; $i<count($imgs); $i++) {
					$img = $imgs[$i];
					$thumb = $thumbs[$i];
					echo '<li><a href="'.$img.'" rel="lightbox[osu2009]" title="OSU Duals, Ohio State University, 15 Nov 2009"><img src="'.$thumb.'"></a></li>'; } ?>
    </ul>
    <h2>EXCO FALL 2009</h2>
    <ul class="photos">
    <?php
					$imgs = glob("photos/excoFall2009/*.*");
					$thumbs = glob("photos/excoFall2009/thumbs/*.*");
					for ($i=0; $i<count($imgs); $i++) {
					$img = $imgs[$i];
					$thumb = $thumbs[$i];
					echo '<li><a href="'.$img.'" rel="lightbox[excoFall2009]" title="Beginning Fencing ExCo, Fall 2009"><img src="'.$thumb.'"></a></li>'; } ?>
    </ul>
    <h2>CHAMPS 2009</h2>
    <ul class="photos">
    <?php
					$imgs = glob("photos/champs2009/*.*");
					$thumbs = glob("photos/champs2009/thumbs/*.*");
					for ($i=0; $i<count($imgs); $i++) {
					$img = $imgs[$i];
					$thumb = $thumbs[$i];
					echo '<li><a href="'.$img.'" rel="lightbox[champs2009]" title="2009 Midwest Fencing Conference Championships, University of Notre Dame, 28 Feb-1 Mar"><img src="'.$thumb.'"></a></li>'; } ?>
    </ul>
    <h2>STABBED IN THE HEART 2009</h2>
    <ul class="photos">
    <?php
					$imgs = glob("photos/stabbed2009/*.*");
					$thumbs = glob("photos/stabbed2009/thumbs/*.*");
					for ($i=0; $i<count($imgs); $i++) {
					$img = $imgs[$i];
					$thumb = $thumbs[$i];
					echo '<li><a href="'.$img.'" rel="lightbox[stabbed2009]" title="Stabbed In The Heart (USFA), 15 Feb 2010, Oberlin College"><img src="'.$thumb.'"></a></li>'; } ?>
	</ul>
<?php include("footer.php"); ?>