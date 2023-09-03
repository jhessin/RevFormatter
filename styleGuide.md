
# REV Bible Verse Styles

This is a list and description of the styles applied to verses on the REV
website. I’m sure it could be improved on, and if I had it to do again, I
certainly would have done some things differently. 

1. Prose. This is a plain text style. Examples of this are throughout the Bible,
   cp most of the gospels.

2. Poetry. Several books in the OT are poetry: Psalms, Proverbs, many of the
   prophets. The verse text is split into an array delimited by [hp] tags
   embedded in the verse text, and each element of the array is wrapped in
   hanging-indent styled <p> tags. There is a small vertical space between
   verses. 

3. Poetry_NB. This is the same as poetry except there is no small vertical space
   at the end of the verse (cp Prov. 1:1-6, 8-19). 

4. BR_Poetry. This is the same as poetry except there is a <br> inserted before
   the verse number, creating a space separating the verse further from the
   previous verse (cp Gen 9:6, 26; 49:18, 19, 20, 21, 22; Prov 24:7).

5. BR_Poetry_NB. This is a combination of both styles 3 and 4 (cp Num. 26:5, 12;
   Prov 1:7, 8, 20). 

6. List. These are somewhat similar to poetry in that they are
   indented, but there is no hanging indent. There are not a lot of them in the
   Bible, and if I had it to do over again I probably would have come up with
   something else. 1 Chron. 1: 14, 15, 19, 20…). 

7. List_END. This denotes the end of a list “paragraph,” so-to-speak. 1 Chron.
   1:12, 16 

8. BR_List. This starts a new list paragraph. 1 Chron. 1:11, 13, 18 

9. BR_List_END. This combines styles 7 & 8.

Also, there is a paragraph flag (0 or 1) for each verse. If 1, the verse begins
a new paragraph. 

There are several inline tags that may be in verses: 

- [pg] inserts a <p> tag (cp Gen. 3:13; Luke 20:15). 

- [hp] indicates a new poetry stanza. 

- [hpbegin] indicates that the poetry starts mid-verse (cp Gen. 2:23; Amos 9:1). 

- [hpend] indicates the poetry ends mid-verse (cp Gen 14:20; Isa. 31:9).

- [lb] indicates a line-break in List styles. 

- [listbegin] indicates the list begins mid-verse (cp 1 Chron. 1:51; 2 Chron.
  17:14). 

- [listend] indicates the list ends mid-verse (cp 1 Chron. 5:6; Neh. 12:7). 

- [bq] indicates the start of a <blockquote> (Exod. 34:6; Deut. 9:26). 

- [/bq] indicates the end of a </blockquote> (Exod. 34:7; Deut. 9:29). 

- [br] inserts a <br> tag (cp Ps. 91:9; Ezek. 21:30). 

- [separator] this is rare… only one verse: Prov. 22:22. Jerry was going to use
  a lot of these, but never got around to it. 

- [mvh] This indicates the location of an outline heading in a verse (Mark
  3:19). If the verse has a heading but no [mvh] tag, the heading goes before
  the beginning of the verse (Mark 3:22). 

- [mvs] This is just like the [mvh] tag, but it’s for superscripts instead of
  headings (verse 1 of many Psalms, Song 1:4, 5). 

- ~ If a verse begins with a tilde, that verse is not in the text and is grayed
  out (Acts 24:7). 

- [[ and/or ]] Double brackets in a verse indicate the start or end of words
  that are not in the text. That part of the verse is grayed out (Acts 24:6-8).
