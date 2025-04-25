## FontBakery report

fontbakery version: 0.13.2







## Check results



<details><summary>[20] Firjar[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Axes and named instances fall within correct ranges? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fvar-regular-coords-correct">opentype/fvar/regular_coords_correct</a></summary>
    <div>







* 🔥 **FAIL** <p>Regular instance has wdth coordinate of 75.0, expected 100</p>
 [code: wdth-not-100]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check glyphs do not have duplicate components which have the same x,y coordinates. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-glyf-non-transformed-duplicate-components">opentype/glyf_non_transformed_duplicate_components</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs have duplicate components which have the same x,y coordinates:
* {'glyph': 'ellipsis', 'component': 'period', 'x': 0, 'y': 0}
* {'glyph': 'ellipsis', 'component': 'period', 'x': 0, 'y': 0}
* {'glyph': 'quotesinglbase', 'component': 'comma', 'x': 0, 'y': 0}
* {'glyph': 'quotedblbase', 'component': 'comma', 'x': 0, 'y': 0}
* {'glyph': 'guillemotleft', 'component': 'guilsinglleft', 'x': 0, 'y': 0} and {'glyph': 'guillemotright', 'component': 'guilsinglright', 'x': 0, 'y': 0}</p>
 [code: found-duplicates]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value 1050 is too large. It should be less than double the yMin. Current absolute yMin value is 285</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_TransLatin_Pinyin glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Positional forms for Arabic letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ئ‍' with features: -init and shaping the text 'ئ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ب‍' with features: -init and shaping the text 'ب‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ت‍' with features: -init and shaping the text 'ت‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ث‍' with features: -init and shaping the text 'ث‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ج‍' with features: -init and shaping the text 'ج‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ح‍' with features: -init and shaping the text 'ح‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'خ‍' with features: -init and shaping the text 'خ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'س‍' with features: -init and shaping the text 'س‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ش‍' with features: -init and shaping the text 'ش‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ص‍' with features: -init and shaping the text 'ص‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ض‍' with features: -init and shaping the text 'ض‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ط‍' with features: -init and shaping the text 'ط‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ظ‍' with features: -init and shaping the text 'ظ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ع‍' with features: -init and shaping the text 'ع‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'غ‍' with features: -init and shaping the text 'غ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ف‍' with features: -init and shaping the text 'ف‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ق‍' with features: -init and shaping the text 'ق‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ك‍' with features: -init and shaping the text 'ك‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ل‍' with features: -init and shaping the text 'ل‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'م‍' with features: -init and shaping the text 'م‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ن‍' with features: -init and shaping the text 'ن‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ه‍' with features: -init and shaping the text 'ه‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ى‍' with features: -init and shaping the text 'ى‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ي‍' with features: -init and shaping the text 'ي‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ئ‍' with features: -medi and shaping the text '‍ئ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ب‍' with features: -medi and shaping the text '‍ب‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ت‍' with features: -medi and shaping the text '‍ت‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ث‍' with features: -medi and shaping the text '‍ث‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ج‍' with features: -medi and shaping the text '‍ج‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ح‍' with features: -medi and shaping the text '‍ح‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍خ‍' with features: -medi and shaping the text '‍خ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍س‍' with features: -medi and shaping the text '‍س‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ش‍' with features: -medi and shaping the text '‍ش‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ص‍' with features: -medi and shaping the text '‍ص‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ض‍' with features: -medi and shaping the text '‍ض‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ط‍' with features: -medi and shaping the text '‍ط‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ظ‍' with features: -medi and shaping the text '‍ظ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ع‍' with features: -medi and shaping the text '‍ع‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍غ‍' with features: -medi and shaping the text '‍غ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ف‍' with features: -medi and shaping the text '‍ف‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ق‍' with features: -medi and shaping the text '‍ق‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ك‍' with features: -medi and shaping the text '‍ك‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ل‍' with features: -medi and shaping the text '‍ل‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍م‍' with features: -medi and shaping the text '‍م‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ن‍' with features: -medi and shaping the text '‍ن‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ه‍' with features: -medi and shaping the text '‍ه‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ى‍' with features: -medi and shaping the text '‍ى‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ي‍' with features: -medi and shaping the text '‍ي‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍أ' with features: -fina and shaping the text '‍أ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ؤ' with features: -fina and shaping the text '‍ؤ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍إ' with features: -fina and shaping the text '‍إ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ئ' with features: -fina and shaping the text '‍ئ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ا' with features: -fina and shaping the text '‍ا', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍آ' with features: -fina and shaping the text '‍آ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ب' with features: -fina and shaping the text '‍ب', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ة' with features: -fina and shaping the text '‍ة', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ت' with features: -fina and shaping the text '‍ت', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ث' with features: -fina and shaping the text '‍ث', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ج' with features: -fina and shaping the text '‍ج', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ح' with features: -fina and shaping the text '‍ح', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍خ' with features: -fina and shaping the text '‍خ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍د' with features: -fina and shaping the text '‍د', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ذ' with features: -fina and shaping the text '‍ذ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ر' with features: -fina and shaping the text '‍ر', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ز' with features: -fina and shaping the text '‍ز', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍س' with features: -fina and shaping the text '‍س', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ش' with features: -fina and shaping the text '‍ش', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ص' with features: -fina and shaping the text '‍ص', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ض' with features: -fina and shaping the text '‍ض', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ط' with features: -fina and shaping the text '‍ط', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ظ' with features: -fina and shaping the text '‍ظ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ع' with features: -fina and shaping the text '‍ع', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍غ' with features: -fina and shaping the text '‍غ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ف' with features: -fina and shaping the text '‍ف', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ق' with features: -fina and shaping the text '‍ق', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ك' with features: -fina and shaping the text '‍ك', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ل' with features: -fina and shaping the text '‍ل', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍م' with features: -fina and shaping the text '‍م', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ن' with features: -fina and shaping the text '‍ن', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ه' with features: -fina and shaping the text '‍ه', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍و' with features: -fina and shaping the text '‍و', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ى' with features: -fina and shaping the text '‍ى', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ي' with features: -fina and shaping the text '‍ي', the output is expected to be different, but was the same</td>
<td align="left">ar_Arab (Arabic)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: گ</td>
<td align="left">fa_Arab (Persian) and ur_Arab (Urdu)</td>
</tr>
<tr>
<td align="left">Positional forms for Arabic letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ئ‍' with features: -init and shaping the text 'ئ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ب‍' with features: -init and shaping the text 'ب‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'پ‍' with features: -init and shaping the text 'پ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ت‍' with features: -init and shaping the text 'ت‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ث‍' with features: -init and shaping the text 'ث‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ج‍' with features: -init and shaping the text 'ج‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'چ‍' with features: -init and shaping the text 'چ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ح‍' with features: -init and shaping the text 'ح‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'خ‍' with features: -init and shaping the text 'خ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'س‍' with features: -init and shaping the text 'س‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ش‍' with features: -init and shaping the text 'ش‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ص‍' with features: -init and shaping the text 'ص‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ض‍' with features: -init and shaping the text 'ض‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ط‍' with features: -init and shaping the text 'ط‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ظ‍' with features: -init and shaping the text 'ظ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ع‍' with features: -init and shaping the text 'ع‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'غ‍' with features: -init and shaping the text 'غ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ف‍' with features: -init and shaping the text 'ف‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ق‍' with features: -init and shaping the text 'ق‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ک‍' with features: -init and shaping the text 'ک‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ل‍' with features: -init and shaping the text 'ل‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'م‍' with features: -init and shaping the text 'م‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ن‍' with features: -init and shaping the text 'ن‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ه‍' with features: -init and shaping the text 'ه‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ی‍' with features: -init and shaping the text 'ی‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ئ‍' with features: -medi and shaping the text '‍ئ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ب‍' with features: -medi and shaping the text '‍ب‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍پ‍' with features: -medi and shaping the text '‍پ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ت‍' with features: -medi and shaping the text '‍ت‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ث‍' with features: -medi and shaping the text '‍ث‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ج‍' with features: -medi and shaping the text '‍ج‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍چ‍' with features: -medi and shaping the text '‍چ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ح‍' with features: -medi and shaping the text '‍ح‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍خ‍' with features: -medi and shaping the text '‍خ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍س‍' with features: -medi and shaping the text '‍س‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ش‍' with features: -medi and shaping the text '‍ش‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ص‍' with features: -medi and shaping the text '‍ص‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ض‍' with features: -medi and shaping the text '‍ض‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ط‍' with features: -medi and shaping the text '‍ط‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ظ‍' with features: -medi and shaping the text '‍ظ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ع‍' with features: -medi and shaping the text '‍ع‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍غ‍' with features: -medi and shaping the text '‍غ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ف‍' with features: -medi and shaping the text '‍ف‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ق‍' with features: -medi and shaping the text '‍ق‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ک‍' with features: -medi and shaping the text '‍ک‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ل‍' with features: -medi and shaping the text '‍ل‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍م‍' with features: -medi and shaping the text '‍م‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ن‍' with features: -medi and shaping the text '‍ن‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ه‍' with features: -medi and shaping the text '‍ه‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ی‍' with features: -medi and shaping the text '‍ی‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍آ' with features: -fina and shaping the text '‍آ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ا' with features: -fina and shaping the text '‍ا', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍أ' with features: -fina and shaping the text '‍أ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ؤ' with features: -fina and shaping the text '‍ؤ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ئ' with features: -fina and shaping the text '‍ئ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ب' with features: -fina and shaping the text '‍ب', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍پ' with features: -fina and shaping the text '‍پ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ت' with features: -fina and shaping the text '‍ت', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ث' with features: -fina and shaping the text '‍ث', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ج' with features: -fina and shaping the text '‍ج', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍چ' with features: -fina and shaping the text '‍چ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ح' with features: -fina and shaping the text '‍ح', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍خ' with features: -fina and shaping the text '‍خ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍د' with features: -fina and shaping the text '‍د', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ذ' with features: -fina and shaping the text '‍ذ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ر' with features: -fina and shaping the text '‍ر', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ز' with features: -fina and shaping the text '‍ز', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ژ' with features: -fina and shaping the text '‍ژ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍س' with features: -fina and shaping the text '‍س', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ش' with features: -fina and shaping the text '‍ش', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ص' with features: -fina and shaping the text '‍ص', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ض' with features: -fina and shaping the text '‍ض', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ط' with features: -fina and shaping the text '‍ط', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ظ' with features: -fina and shaping the text '‍ظ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ع' with features: -fina and shaping the text '‍ع', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍غ' with features: -fina and shaping the text '‍غ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ف' with features: -fina and shaping the text '‍ف', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ق' with features: -fina and shaping the text '‍ق', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ک' with features: -fina and shaping the text '‍ک', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ل' with features: -fina and shaping the text '‍ل', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍م' with features: -fina and shaping the text '‍م', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ن' with features: -fina and shaping the text '‍ن', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍و' with features: -fina and shaping the text '‍و', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ه' with features: -fina and shaping the text '‍ه', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ة' with features: -fina and shaping the text '‍ة', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ی' with features: -fina and shaping the text '‍ی', the output is expected to be different, but was the same</td>
<td align="left">fa_Arab (Persian)</td>
</tr>
<tr>
<td align="left">Positional forms for Arabic letters:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ب‍' with features: -init and shaping the text 'ب‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'پ‍' with features: -init and shaping the text 'پ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ت‍' with features: -init and shaping the text 'ت‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ٹ‍' with features: -init and shaping the text 'ٹ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ث‍' with features: -init and shaping the text 'ث‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ج‍' with features: -init and shaping the text 'ج‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'چ‍' with features: -init and shaping the text 'چ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ح‍' with features: -init and shaping the text 'ح‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'خ‍' with features: -init and shaping the text 'خ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'س‍' with features: -init and shaping the text 'س‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ش‍' with features: -init and shaping the text 'ش‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ص‍' with features: -init and shaping the text 'ص‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ض‍' with features: -init and shaping the text 'ض‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ط‍' with features: -init and shaping the text 'ط‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ظ‍' with features: -init and shaping the text 'ظ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ع‍' with features: -init and shaping the text 'ع‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'غ‍' with features: -init and shaping the text 'غ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ف‍' with features: -init and shaping the text 'ف‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ق‍' with features: -init and shaping the text 'ق‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ک‍' with features: -init and shaping the text 'ک‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ل‍' with features: -init and shaping the text 'ل‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'م‍' with features: -init and shaping the text 'م‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ن‍' with features: -init and shaping the text 'ن‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ہ‍' with features: -init and shaping the text 'ہ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ھ‍' with features: -init and shaping the text 'ھ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text 'ی‍' with features: -init and shaping the text 'ی‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ب‍' with features: -medi and shaping the text '‍ب‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍پ‍' with features: -medi and shaping the text '‍پ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ت‍' with features: -medi and shaping the text '‍ت‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ٹ‍' with features: -medi and shaping the text '‍ٹ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ث‍' with features: -medi and shaping the text '‍ث‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ج‍' with features: -medi and shaping the text '‍ج‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍چ‍' with features: -medi and shaping the text '‍چ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ح‍' with features: -medi and shaping the text '‍ح‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍خ‍' with features: -medi and shaping the text '‍خ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍س‍' with features: -medi and shaping the text '‍س‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ش‍' with features: -medi and shaping the text '‍ش‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ص‍' with features: -medi and shaping the text '‍ص‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ض‍' with features: -medi and shaping the text '‍ض‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ط‍' with features: -medi and shaping the text '‍ط‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ظ‍' with features: -medi and shaping the text '‍ظ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ع‍' with features: -medi and shaping the text '‍ع‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍غ‍' with features: -medi and shaping the text '‍غ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ف‍' with features: -medi and shaping the text '‍ف‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ق‍' with features: -medi and shaping the text '‍ق‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ک‍' with features: -medi and shaping the text '‍ک‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ل‍' with features: -medi and shaping the text '‍ل‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍م‍' with features: -medi and shaping the text '‍م‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ن‍' with features: -medi and shaping the text '‍ن‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ہ‍' with features: -medi and shaping the text '‍ہ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ھ‍' with features: -medi and shaping the text '‍ھ‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ی‍' with features: -medi and shaping the text '‍ی‍', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ا' with features: -fina and shaping the text '‍ا', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ب' with features: -fina and shaping the text '‍ب', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍پ' with features: -fina and shaping the text '‍پ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ت' with features: -fina and shaping the text '‍ت', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ٹ' with features: -fina and shaping the text '‍ٹ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ث' with features: -fina and shaping the text '‍ث', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ج' with features: -fina and shaping the text '‍ج', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍چ' with features: -fina and shaping the text '‍چ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ح' with features: -fina and shaping the text '‍ح', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍خ' with features: -fina and shaping the text '‍خ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍د' with features: -fina and shaping the text '‍د', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ڈ' with features: -fina and shaping the text '‍ڈ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ذ' with features: -fina and shaping the text '‍ذ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ر' with features: -fina and shaping the text '‍ر', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ڑ' with features: -fina and shaping the text '‍ڑ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ز' with features: -fina and shaping the text '‍ز', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ژ' with features: -fina and shaping the text '‍ژ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍س' with features: -fina and shaping the text '‍س', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ش' with features: -fina and shaping the text '‍ش', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ص' with features: -fina and shaping the text '‍ص', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ض' with features: -fina and shaping the text '‍ض', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ط' with features: -fina and shaping the text '‍ط', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ظ' with features: -fina and shaping the text '‍ظ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ع' with features: -fina and shaping the text '‍ع', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍غ' with features: -fina and shaping the text '‍غ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ف' with features: -fina and shaping the text '‍ف', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ق' with features: -fina and shaping the text '‍ق', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ک' with features: -fina and shaping the text '‍ک', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ل' with features: -fina and shaping the text '‍ل', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍م' with features: -fina and shaping the text '‍م', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ن' with features: -fina and shaping the text '‍ن', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍و' with features: -fina and shaping the text '‍و', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ہ' with features: -fina and shaping the text '‍ہ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ھ' with features: -fina and shaping the text '‍ھ', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ی' with features: -fina and shaping the text '‍ی', the output is expected to be different, but was the same</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">When shaping the text '‍ے' with features: -fina and shaping the text '‍ے', the output is expected to be different, but was the same</td>
<td align="left">ur_Arab (Urdu)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_TransLatin_Pinyin glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ڜ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ڢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ڥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ڧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ڨ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: گ</td>
<td align="left">ar_Arab (Arabic)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni064E to .notdef when shaping the text '◌َ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0650 to .notdef when shaping the text '◌ِ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni064F to .notdef when shaping the text '◌ُ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0652 to .notdef when shaping the text '◌ْ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0656 to the base glyph when shaping the text '◌ٖ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0670 to .notdef when shaping the text '◌ٰ'</td>
<td align="left">fa_Arab (Persian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ؀؁؂؃‌‍‏</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ٗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ٻ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ٺ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ټ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ٽ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni064B to .notdef when shaping the text '◌ً'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni064C to .notdef when shaping the text '◌ٌ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni064D to .notdef when shaping the text '◌ٍ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni064E to .notdef when shaping the text '◌َ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni064F to .notdef when shaping the text '◌ُ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0650 to .notdef when shaping the text '◌ِ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0651 to .notdef when shaping the text '◌ّ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0652 to .notdef when shaping the text '◌ْ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0654 to .notdef when shaping the text '◌ٔ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0656 to the base glyph when shaping the text '◌ٖ'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0658 to the base glyph when shaping the text '◌٘'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0670 to .notdef when shaping the text '◌ٰ'</td>
<td align="left">ur_Arab (Urdu)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright 20** the my font project authors (<a href="https://github.com/googlefonts/googlefonts-project-template">https://github.com/googlefonts/googlefonts-project-template</a>)&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-names">googlefonts/font_names</a></summary>
    <div>







* 🔥 **FAIL** <p>Font names are incorrect:</p>
<table>
<thead>
<tr>
<th align="left">nameID</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Family Name</td>
<td align="left"><strong>Firjar Thin</strong></td>
<td align="left"><strong>Firjar Condensed Thin</strong></td>
</tr>
<tr>
<td align="left">Subfamily Name</td>
<td align="left">Regular</td>
<td align="left">Regular</td>
</tr>
<tr>
<td align="left">Full Name</td>
<td align="left"><strong>Firjar Thin</strong></td>
<td align="left"><strong>Firjar Condensed Thin</strong></td>
</tr>
<tr>
<td align="left">Postscript Name</td>
<td align="left"><strong>Firjar-Thin</strong></td>
<td align="left"><strong>Firjar-CondensedThin</strong></td>
</tr>
<tr>
<td align="left">Typographic Family Name</td>
<td align="left">Firjar</td>
<td align="left">Firjar</td>
</tr>
<tr>
<td align="left">Typographic Subfamily Name</td>
<td align="left"><strong>Thin</strong></td>
<td align="left"><strong>Condensed Thin</strong></td>
</tr>
</tbody>
</table>
 [code: bad-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyph-coverage">googlefonts/glyph_coverage</a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x00A7 (SECTION SIGN)


- 0x00A8 (DIAERESIS)


- 0x00AA (FEMININE ORDINAL INDICATOR)


- 0x00AF (MACRON)


- 0x00B4 (ACUTE ACCENT)


- 0x00B6 (PILCROW SIGN)


- 0x00B8 (CEDILLA)


- 0x00BA (MASCULINE ORDINAL INDICATOR)


- 0x00C0 (LATIN CAPITAL LETTER A WITH GRAVE)


- 0x00C1 (LATIN CAPITAL LETTER A WITH ACUTE)


- 0x00C2 (LATIN CAPITAL LETTER A WITH CIRCUMFLEX)


- 0x00C3 (LATIN CAPITAL LETTER A WITH TILDE)


- 0x00C4 (LATIN CAPITAL LETTER A WITH DIAERESIS)


- 0x00C5 (LATIN CAPITAL LETTER A WITH RING ABOVE)


- 0x00C6 (LATIN CAPITAL LETTER AE)


- 0x00C7 (LATIN CAPITAL LETTER C WITH CEDILLA)


- 0x00C8 (LATIN CAPITAL LETTER E WITH GRAVE)


- 0x00C9 (LATIN CAPITAL LETTER E WITH ACUTE)


- 0x00CA (LATIN CAPITAL LETTER E WITH CIRCUMFLEX)


- 0x00CB (LATIN CAPITAL LETTER E WITH DIAERESIS)


- 0x00CC (LATIN CAPITAL LETTER I WITH GRAVE)


- 0x00CD (LATIN CAPITAL LETTER I WITH ACUTE)


- 0x00CE (LATIN CAPITAL LETTER I WITH CIRCUMFLEX)


- 0x00CF (LATIN CAPITAL LETTER I WITH DIAERESIS)


- 0x00D0 (LATIN CAPITAL LETTER ETH)


- 0x00D1 (LATIN CAPITAL LETTER N WITH TILDE)


- 0x00D2 (LATIN CAPITAL LETTER O WITH GRAVE)


- 0x00D3 (LATIN CAPITAL LETTER O WITH ACUTE)


- 0x00D4 (LATIN CAPITAL LETTER O WITH CIRCUMFLEX)


- 0x00D5 (LATIN CAPITAL LETTER O WITH TILDE)


- 0x00D6 (LATIN CAPITAL LETTER O WITH DIAERESIS)


- 0x00D8 (LATIN CAPITAL LETTER O WITH STROKE)


- 0x00D9 (LATIN CAPITAL LETTER U WITH GRAVE)


- 0x00DA (LATIN CAPITAL LETTER U WITH ACUTE)


- 0x00DB (LATIN CAPITAL LETTER U WITH CIRCUMFLEX)


- 0x00DC (LATIN CAPITAL LETTER U WITH DIAERESIS)


- 0x00DD (LATIN CAPITAL LETTER Y WITH ACUTE)


- 0x00DE (LATIN CAPITAL LETTER THORN)


- 0x00DF (LATIN SMALL LETTER SHARP S)


- 0x00E0 (LATIN SMALL LETTER A WITH GRAVE)


- 0x00E1 (LATIN SMALL LETTER A WITH ACUTE)


- 0x00E2 (LATIN SMALL LETTER A WITH CIRCUMFLEX)


- 0x00E3 (LATIN SMALL LETTER A WITH TILDE)


- 0x00E4 (LATIN SMALL LETTER A WITH DIAERESIS)


- 0x00E5 (LATIN SMALL LETTER A WITH RING ABOVE)


- 0x00E6 (LATIN SMALL LETTER AE)


- 0x00E7 (LATIN SMALL LETTER C WITH CEDILLA)


- 0x00E8 (LATIN SMALL LETTER E WITH GRAVE)


- 0x00E9 (LATIN SMALL LETTER E WITH ACUTE)


- 0x00EA (LATIN SMALL LETTER E WITH CIRCUMFLEX)


- 0x00EB (LATIN SMALL LETTER E WITH DIAERESIS)


- 0x00EC (LATIN SMALL LETTER I WITH GRAVE)


- 0x00ED (LATIN SMALL LETTER I WITH ACUTE)


- 0x00EE (LATIN SMALL LETTER I WITH CIRCUMFLEX)


- 0x00EF (LATIN SMALL LETTER I WITH DIAERESIS)


- 0x00F0 (LATIN SMALL LETTER ETH)


- 0x00F1 (LATIN SMALL LETTER N WITH TILDE)


- 0x00F2 (LATIN SMALL LETTER O WITH GRAVE)


- 0x00F3 (LATIN SMALL LETTER O WITH ACUTE)


- 0x00F4 (LATIN SMALL LETTER O WITH CIRCUMFLEX)


- 0x00F5 (LATIN SMALL LETTER O WITH TILDE)


- 0x00F6 (LATIN SMALL LETTER O WITH DIAERESIS)


- 0x00F8 (LATIN SMALL LETTER O WITH STROKE)


- 0x00F9 (LATIN SMALL LETTER U WITH GRAVE)


- 0x00FA (LATIN SMALL LETTER U WITH ACUTE)


- 0x00FB (LATIN SMALL LETTER U WITH CIRCUMFLEX)


- 0x00FC (LATIN SMALL LETTER U WITH DIAERESIS)


- 0x00FD (LATIN SMALL LETTER Y WITH ACUTE)


- 0x00FE (LATIN SMALL LETTER THORN)


- 0x00FF (LATIN SMALL LETTER Y WITH DIAERESIS)


- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


- 0x0101 (LATIN SMALL LETTER A WITH MACRON)


- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


- 0x0103 (LATIN SMALL LETTER A WITH BREVE)


- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


- 0x0105 (LATIN SMALL LETTER A WITH OGONEK)


- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)


- 0x0107 (LATIN SMALL LETTER C WITH ACUTE)


- 0x010A (LATIN CAPITAL LETTER C WITH DOT ABOVE)


- 0x010B (LATIN SMALL LETTER C WITH DOT ABOVE)


- 0x010C (LATIN CAPITAL LETTER C WITH CARON)


- 0x010D (LATIN SMALL LETTER C WITH CARON)


- 0x010E (LATIN CAPITAL LETTER D WITH CARON)


- 0x010F (LATIN SMALL LETTER D WITH CARON)


- 0x0110 (LATIN CAPITAL LETTER D WITH STROKE)


- 0x0111 (LATIN SMALL LETTER D WITH STROKE)


- 0x0112 (LATIN CAPITAL LETTER E WITH MACRON)


- 0x0113 (LATIN SMALL LETTER E WITH MACRON)


- 0x0116 (LATIN CAPITAL LETTER E WITH DOT ABOVE)


- 0x0117 (LATIN SMALL LETTER E WITH DOT ABOVE)


- 0x0118 (LATIN CAPITAL LETTER E WITH OGONEK)


- 0x0119 (LATIN SMALL LETTER E WITH OGONEK)


- 0x011A (LATIN CAPITAL LETTER E WITH CARON)


- 0x011B (LATIN SMALL LETTER E WITH CARON)


- 0x011E (LATIN CAPITAL LETTER G WITH BREVE)


- 0x011F (LATIN SMALL LETTER G WITH BREVE)


- 0x0120 (LATIN CAPITAL LETTER G WITH DOT ABOVE)


- 0x0121 (LATIN SMALL LETTER G WITH DOT ABOVE)


- 0x0122 (LATIN CAPITAL LETTER G WITH CEDILLA)


- 0x0123 (LATIN SMALL LETTER G WITH CEDILLA)


- 0x0126 (LATIN CAPITAL LETTER H WITH STROKE)


- 0x0127 (LATIN SMALL LETTER H WITH STROKE)


- 0x012A (LATIN CAPITAL LETTER I WITH MACRON)


- 0x012B (LATIN SMALL LETTER I WITH MACRON)


- 0x012E (LATIN CAPITAL LETTER I WITH OGONEK)


- 0x012F (LATIN SMALL LETTER I WITH OGONEK)


- 0x0130 (LATIN CAPITAL LETTER I WITH DOT ABOVE)


- 0x0131 (LATIN SMALL LETTER DOTLESS I)


- 0x0136 (LATIN CAPITAL LETTER K WITH CEDILLA)


- 0x0137 (LATIN SMALL LETTER K WITH CEDILLA)


- 0x0139 (LATIN CAPITAL LETTER L WITH ACUTE)


- 0x013A (LATIN SMALL LETTER L WITH ACUTE)


- 0x013B (LATIN CAPITAL LETTER L WITH CEDILLA)


- 0x013C (LATIN SMALL LETTER L WITH CEDILLA)


- 0x013D (LATIN CAPITAL LETTER L WITH CARON)


- 0x013E (LATIN SMALL LETTER L WITH CARON)


- 0x0141 (LATIN CAPITAL LETTER L WITH STROKE)


- 0x0142 (LATIN SMALL LETTER L WITH STROKE)


- 0x0143 (LATIN CAPITAL LETTER N WITH ACUTE)


- 0x0144 (LATIN SMALL LETTER N WITH ACUTE)


- 0x0145 (LATIN CAPITAL LETTER N WITH CEDILLA)


- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)


- 0x0147 (LATIN CAPITAL LETTER N WITH CARON)


- 0x0148 (LATIN SMALL LETTER N WITH CARON)


- 0x0150 (LATIN CAPITAL LETTER O WITH DOUBLE ACUTE)


- 0x0151 (LATIN SMALL LETTER O WITH DOUBLE ACUTE)


- 0x0152 (LATIN CAPITAL LIGATURE OE)


- 0x0153 (LATIN SMALL LIGATURE OE)


- 0x0154 (LATIN CAPITAL LETTER R WITH ACUTE)


- 0x0155 (LATIN SMALL LETTER R WITH ACUTE)


- 0x0158 (LATIN CAPITAL LETTER R WITH CARON)


- 0x0159 (LATIN SMALL LETTER R WITH CARON)


- 0x015A (LATIN CAPITAL LETTER S WITH ACUTE)


- 0x015B (LATIN SMALL LETTER S WITH ACUTE)


- 0x015E (LATIN CAPITAL LETTER S WITH CEDILLA)


- 0x015F (LATIN SMALL LETTER S WITH CEDILLA)


- 0x0160 (LATIN CAPITAL LETTER S WITH CARON)


- 0x0161 (LATIN SMALL LETTER S WITH CARON)


- 0x0164 (LATIN CAPITAL LETTER T WITH CARON)


- 0x0165 (LATIN SMALL LETTER T WITH CARON)


- 0x016A (LATIN CAPITAL LETTER U WITH MACRON)


- 0x016B (LATIN SMALL LETTER U WITH MACRON)


- 0x016E (LATIN CAPITAL LETTER U WITH RING ABOVE)


- 0x016F (LATIN SMALL LETTER U WITH RING ABOVE)


- 0x0170 (LATIN CAPITAL LETTER U WITH DOUBLE ACUTE)


- 0x0171 (LATIN SMALL LETTER U WITH DOUBLE ACUTE)


- 0x0172 (LATIN CAPITAL LETTER U WITH OGONEK)


- 0x0173 (LATIN SMALL LETTER U WITH OGONEK)


- 0x0174 (LATIN CAPITAL LETTER W WITH CIRCUMFLEX)


- 0x0175 (LATIN SMALL LETTER W WITH CIRCUMFLEX)


- 0x0176 (LATIN CAPITAL LETTER Y WITH CIRCUMFLEX)


- 0x0177 (LATIN SMALL LETTER Y WITH CIRCUMFLEX)


- 0x0178 (LATIN CAPITAL LETTER Y WITH DIAERESIS)


- 0x0179 (LATIN CAPITAL LETTER Z WITH ACUTE)


- 0x017A (LATIN SMALL LETTER Z WITH ACUTE)


- 0x017B (LATIN CAPITAL LETTER Z WITH DOT ABOVE)


- 0x017C (LATIN SMALL LETTER Z WITH DOT ABOVE)


- 0x017D (LATIN CAPITAL LETTER Z WITH CARON)


- 0x017E (LATIN SMALL LETTER Z WITH CARON)


- 0x0218 (LATIN CAPITAL LETTER S WITH COMMA BELOW)


- 0x0219 (LATIN SMALL LETTER S WITH COMMA BELOW)


- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)


- 0x021B (LATIN SMALL LETTER T WITH COMMA BELOW)


- 0x0237 (LATIN SMALL LETTER DOTLESS J)


- 0x02C6 (MODIFIER LETTER CIRCUMFLEX ACCENT)


- 0x02C7 (CARON)


- 0x02D8 (BREVE)


- 0x02D9 (DOT ABOVE)


- 0x02DA (RING ABOVE)


- 0x02DB (OGONEK)


- 0x02DC (SMALL TILDE)


- 0x02DD (DOUBLE ACUTE ACCENT)


- 0x0300 (COMBINING GRAVE ACCENT)


- 0x0301 (COMBINING ACUTE ACCENT)


- 0x0302 (COMBINING CIRCUMFLEX ACCENT)


- 0x0303 (COMBINING TILDE)


- 0x0304 (COMBINING MACRON)


- 0x0306 (COMBINING BREVE)


- 0x0307 (COMBINING DOT ABOVE)


- 0x0308 (COMBINING DIAERESIS)


- 0x030A (COMBINING RING ABOVE)


- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


- 0x030C (COMBINING CARON)


- 0x0326 (COMBINING COMMA BELOW)


- 0x0327 (COMBINING CEDILLA)


- 0x0328 (COMBINING OGONEK)


- 0x1E80 (LATIN CAPITAL LETTER W WITH GRAVE)


- 0x1E81 (LATIN SMALL LETTER W WITH GRAVE)


- 0x1E82 (LATIN CAPITAL LETTER W WITH ACUTE)


- 0x1E83 (LATIN SMALL LETTER W WITH ACUTE)


- 0x1E84 (LATIN CAPITAL LETTER W WITH DIAERESIS)


- 0x1E85 (LATIN SMALL LETTER W WITH DIAERESIS)


- 0x1E9E (LATIN CAPITAL LETTER SHARP S)


- 0x1EF2 (LATIN CAPITAL LETTER Y WITH GRAVE)


- 0x1EF3 (LATIN SMALL LETTER Y WITH GRAVE)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>Axis Value for 'wdth':'Condensed' is expected to be '75.0' but this font has 'Condensed'='70.0'.</p>
 [code: bad-coordinate]



* 🔥 **FAIL** <p>Axis Value for 'wdth':'Expanded' is expected to be '125.0' but this font has 'Expanded'='120.0'.</p>
 [code: bad-coordinate]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking post.italicAngle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-italic-angle">opentype/italic_angle</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs were present but did not contain any outlines: bar</p>
 [code: empty-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if uppercase glyphs are vertically centered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#caps-vertically-centered">caps_vertically_centered</a></summary>
    <div>







* ⚠️ **WARN** <p>Uppercase glyphs are not vertically centered in the em box.</p>
 [code: vertical-metrics-not-centered]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour order differs in glyph 'k': [0, 1, 2] in wght=100,wdth=75, [0, 2, 1] in wght=100,wdth=125.

- Contour order differs in glyph 'k': [0, 1, 2] in wght=100,wdth=125, [0, 2, 1] in wght=442,wdth=75.

- Contour order differs in glyph 'k': [0, 1, 2] in wght=900,wdth=75, [0, 2, 1] in wght=442,wdth=125.

- Contour order differs in glyph 'k': [0, 1, 2] in wght=442,wdth=125, [0, 2, 1] in wght=614,wdth=125.

- Contour order differs in glyph 'W': [0, 1] in wght=100,wdth=75, [1, 0] in wght=100,wdth=125.

- Contour order differs in glyph 'W': [0, 1] in wght=100,wdth=125, [1, 0] in wght=442,wdth=75.

- Contour order differs in glyph 'W': [0, 1] in wght=900,wdth=75, [1, 0] in wght=442,wdth=125.
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* S (U+0053): L&lt;&lt;315.0,335.0&gt;--&lt;315.0,305.0&gt;&gt; has the same coordinates as a previous segment.

* s (U+0073): L&lt;&lt;247.0,235.0&gt;--&lt;247.0,205.0&gt;&gt; has the same coordinates as a previous segment.

* uni0635 (U+0635): L&lt;&lt;476.0,360.0&gt;--&lt;506.0,360.0&gt;&gt; has the same coordinates as a previous segment.

* uni0635.fina: L&lt;&lt;476.0,360.0&gt;--&lt;506.0,360.0&gt;&gt; has the same coordinates as a previous segment.

* uni0636 (U+0636): L&lt;&lt;476.0,360.0&gt;--&lt;506.0,360.0&gt;&gt; has the same coordinates as a previous segment.

* uni0636.fina: L&lt;&lt;476.0,360.0&gt;--&lt;506.0,360.0&gt;&gt; has the same coordinates as a previous segment.

* uni0637.medi: L&lt;&lt;27.0,0.0&gt;--&lt;27.0,30.0&gt;&gt; has the same coordinates as a previous segment.

* uni0637.init: L&lt;&lt;27.0,0.0&gt;--&lt;27.0,30.0&gt;&gt; has the same coordinates as a previous segment.

* uni0638.medi: L&lt;&lt;27.0,0.0&gt;--&lt;27.0,30.0&gt;&gt; has the same coordinates as a previous segment.

* uni0638.init: L&lt;&lt;27.0,0.0&gt;--&lt;27.0,30.0&gt;&gt; has the same coordinates as a previous segment.

* uni0639.fina: L&lt;&lt;517.0,30.0&gt;--&lt;517.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0639.medi: L&lt;&lt;462.0,30.0&gt;--&lt;462.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni063A.fina: L&lt;&lt;517.0,30.0&gt;--&lt;517.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni063A.medi: L&lt;&lt;462.0,30.0&gt;--&lt;462.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni066F.fina: L&lt;&lt;573.0,30.0&gt;--&lt;573.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0642.fina: L&lt;&lt;573.0,30.0&gt;--&lt;573.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0664 (U+0664): L&lt;&lt;424.0,360.0&gt;--&lt;424.0,330.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;88.0,-3.0&gt;-&lt;76.0,-3.0&gt;-&lt;68.0,5.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;68.0,5.0&gt;-&lt;60.0,13.0&gt;-&lt;60.0,25.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;60.0,25.0&gt;-&lt;60.0,37.0&gt;-&lt;68.0,45.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;68.0,45.0&gt;-&lt;76.0,53.0&gt;-&lt;88.0,53.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;88.0,53.0&gt;-&lt;99.0,53.0&gt;-&lt;107.5,45.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;107.5,45.0&gt;-&lt;116.0,37.0&gt;-&lt;116.0,25.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;116.0,25.0&gt;-&lt;116.0,13.0&gt;-&lt;107.5,5.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;107.5,5.0&gt;-&lt;99.0,-3.0&gt;-&lt;88.0,-3.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;88.0,-3.0&gt;-&lt;76.0,-3.0&gt;-&lt;68.0,5.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;68.0,5.0&gt;-&lt;60.0,13.0&gt;-&lt;60.0,25.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;60.0,25.0&gt;-&lt;60.0,37.0&gt;-&lt;68.0,45.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;68.0,45.0&gt;-&lt;76.0,53.0&gt;-&lt;88.0,53.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;88.0,53.0&gt;-&lt;99.0,53.0&gt;-&lt;107.5,45.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;107.5,45.0&gt;-&lt;116.0,37.0&gt;-&lt;116.0,25.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;116.0,25.0&gt;-&lt;116.0,13.0&gt;-&lt;107.5,5.0&gt;&gt; has the same coordinates as a previous segment.

* ellipsis (U+2026): B&lt;&lt;107.5,5.0&gt;-&lt;99.0,-3.0&gt;-&lt;88.0,-3.0&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): L&lt;&lt;60.0,-102.0&gt;--&lt;60.0,28.0&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): B&lt;&lt;60.0,28.0&gt;-&lt;60.0,39.0&gt;-&lt;68.0,46.0&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): B&lt;&lt;68.0,46.0&gt;-&lt;76.0,53.0&gt;-&lt;87.0,53.0&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): B&lt;&lt;87.0,53.0&gt;-&lt;98.0,53.0&gt;-&lt;105.5,46.0&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): B&lt;&lt;105.5,46.0&gt;-&lt;113.0,39.0&gt;-&lt;113.0,28.0&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): L&lt;&lt;113.0,28.0&gt;--&lt;113.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): B&lt;&lt;113.0,0.0&gt;-&lt;113.0,-36.0&gt;-&lt;98.0,-63.5&gt;&gt; has the same coordinates as a previous segment.

* quotesinglbase (U+201A): B&lt;&lt;98.0,-63.5&gt;-&lt;83.0,-91.0&gt;-&lt;60.0,-102.0&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): L&lt;&lt;60.0,-102.0&gt;--&lt;60.0,28.0&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): B&lt;&lt;60.0,28.0&gt;-&lt;60.0,39.0&gt;-&lt;68.0,46.0&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): B&lt;&lt;68.0,46.0&gt;-&lt;76.0,53.0&gt;-&lt;87.0,53.0&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): B&lt;&lt;87.0,53.0&gt;-&lt;98.0,53.0&gt;-&lt;105.5,46.0&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): B&lt;&lt;105.5,46.0&gt;-&lt;113.0,39.0&gt;-&lt;113.0,28.0&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): L&lt;&lt;113.0,28.0&gt;--&lt;113.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): B&lt;&lt;113.0,0.0&gt;-&lt;113.0,-36.0&gt;-&lt;98.0,-63.5&gt;&gt; has the same coordinates as a previous segment.

* quotedblbase (U+201E): B&lt;&lt;98.0,-63.5&gt;-&lt;83.0,-91.0&gt;-&lt;60.0,-102.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;277.0,47.0&gt;--&lt;257.0,25.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;257.0,25.0&gt;--&lt;60.0,214.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;60.0,214.0&gt;--&lt;60.0,267.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;60.0,267.0&gt;--&lt;257.0,456.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;257.0,456.0&gt;--&lt;277.0,434.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;277.0,434.0&gt;--&lt;90.0,255.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;90.0,255.0&gt;--&lt;90.0,226.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;90.0,226.0&gt;--&lt;277.0,47.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;60.0,47.0&gt;--&lt;247.0,226.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;247.0,226.0&gt;--&lt;247.0,255.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;247.0,255.0&gt;--&lt;60.0,434.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;60.0,434.0&gt;--&lt;80.0,456.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;80.0,456.0&gt;--&lt;277.0,267.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;277.0,267.0&gt;--&lt;277.0,214.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;277.0,214.0&gt;--&lt;80.0,25.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;80.0,25.0&gt;--&lt;60.0,47.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- dotbelowar

- dotcenterar

- threedotsdownabovear

- threedotsupabovear

- threedotsupbelowar

- twodotshorizontalabovear

- twodotshorizontalbelowar

- twodotsverticalabovear

- twodotsverticalbelowar

- uni0622.fina

- uni0623.fina

- uni0624.fina

- uni0625.fina

- uni0626.fina

- uni0626.init

- uni0626.medi

- uni0627.fina

- uni0628.fina

- uni0628.init

- uni0628.medi

- uni0629.fina

- uni062A.fina

- uni062A.init

- uni062A.medi

- uni062B.fina

- uni062B.init

- uni062B.medi

- uni062C.fina

- uni062C.init

- uni062C.medi

- uni062D.fina

- uni062D.fina.alt

- uni062D.init

- uni062D.medi

- uni062E.fina

- uni062E.init

- uni062E.medi

- uni062F.fina

- uni0630.fina

- uni0631.fina

- uni0632.fina

- uni0633.fina

- uni0633.init

- uni0633.medi

- uni0634.fina

- uni0634.init

- uni0634.medi

- uni0635.fina

- uni0635.init

- uni0635.medi

- uni0636.fina

- uni0636.init

- uni0636.medi

- uni0637.fina

- uni0637.init

- uni0637.medi

- uni0638.fina

- uni0638.init

- uni0638.medi

- uni0639.fina

- uni0639.init

- uni0639.medi

- uni063A.fina

- uni063A.init

- uni063A.medi

- uni0641.fina

- uni0641.init

- uni0641.medi

- uni0642.fina

- uni0642.init

- uni0642.medi

- uni0643.fina

- uni0643.init

- uni0643.medi

- uni0644.fina

- uni0644.init

- uni0644.medi

- uni06440622

- uni06440622.fina

- uni06440623

- uni06440623.fina

- uni06440625

- uni06440625.fina

- uni06440627

- uni06440627.fina

- uni06440671

- uni06440671.fina

- uni0645.fina

- uni0645.init

- uni0645.medi

- uni0646.fina

- uni0646.init

- uni0646.medi

- uni0647.fina

- uni0647.medi

- uni0648.fina

- uni0649.fina

- uni064A.fina

- uni064A.init

- uni064A.medi

- uni0651064B

- uni0651064C

- uni0651064D

- uni0651064E

- uni0651064F

- uni06510650

- uni06510670

- uni0654064B

- uni0654064C

- uni0654064E

- uni0654064F

- uni06540652

- uni0655064D

- uni06550650

- uni066E.fina

- uni066E.init

- uni066E.medi

- uni066F.fina

- uni0671.fina

- uni0679.fina

- uni0679.init

- uni0679.medi

- uni067E.fina

- uni067E.init

- uni067E.medi

- uni0686.fina

- uni0686.init

- uni0686.medi

- uni0688.fina

- uni068E.fina

- uni0691.fina

- uni0698.fina

- uni06A1.fina

- uni06A1.init

- uni06A1.medi

- uni06A4.fina

- uni06A4.init

- uni06A4.medi

- uni06A9.fina

- uni06A9.init

- uni06A9.medi

- uni06BA.fina

- uni06C1.fina

- uni06C2.fina

- uni06C3.fina

- uni06CA.fina

- uni06CC.fina

- uni06CC.init

- uni06CC.medi

- uni06CF.fina

- uni06D2.fina

- uni06D3.fina

- uni06D5.fina

- uni06F4.urdu

- uni06F7.urdu
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+0609 ARABIC-INDIC PER MILLE SIGN: try adding arabic</li>
<li>U+060C ARABIC COMMA: try adding one of: arabic, hanifi-rohingya, thaana, nko, yezidi, syriac, garay</li>
<li>U+060D ARABIC DATE SEPARATOR: try adding arabic</li>
<li>U+0615 ARABIC SMALL HIGH TAH: try adding arabic</li>
<li>U+061B ARABIC SEMICOLON: try adding one of: arabic, hanifi-rohingya, thaana, nko, yezidi, syriac, garay</li>
<li>U+061F ARABIC QUESTION MARK: try adding one of: arabic, hanifi-rohingya, thaana, nko, yezidi, syriac, garay, adlam</li>
<li>U+0621 ARABIC LETTER HAMZA: try adding one of: syriac, arabic</li>
<li>U+0622 ARABIC LETTER ALEF WITH MADDA ABOVE: try adding arabic</li>
<li>U+0623 ARABIC LETTER ALEF WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0624 ARABIC LETTER WAW WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0625 ARABIC LETTER ALEF WITH HAMZA BELOW: try adding arabic</li>
<li>U+0626 ARABIC LETTER YEH WITH HAMZA ABOVE: try adding arabic</li>
<li>U+0627 ARABIC LETTER ALEF: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+0628 ARABIC LETTER BEH: try adding arabic</li>
<li>U+0629 ARABIC LETTER TEH MARBUTA: try adding arabic</li>
<li>U+062A ARABIC LETTER TEH: try adding arabic</li>
<li>U+062B ARABIC LETTER THEH: try adding arabic</li>
<li>U+062C ARABIC LETTER JEEM: try adding arabic</li>
<li>U+062D ARABIC LETTER HAH: try adding arabic</li>
<li>U+062E ARABIC LETTER KHAH: try adding arabic</li>
<li>U+062F ARABIC LETTER DAL: try adding arabic</li>
<li>U+0630 ARABIC LETTER THAL: try adding arabic</li>
<li>U+0631 ARABIC LETTER REH: try adding arabic</li>
<li>U+0632 ARABIC LETTER ZAIN: try adding arabic</li>
<li>U+0633 ARABIC LETTER SEEN: try adding arabic</li>
<li>U+0634 ARABIC LETTER SHEEN: try adding arabic</li>
<li>U+0635 ARABIC LETTER SAD: try adding arabic</li>
<li>U+0636 ARABIC LETTER DAD: try adding arabic</li>
<li>U+0637 ARABIC LETTER TAH: try adding arabic</li>
<li>U+0638 ARABIC LETTER ZAH: try adding arabic</li>
<li>U+0639 ARABIC LETTER AIN: try adding arabic</li>
<li>U+063A ARABIC LETTER GHAIN: try adding arabic</li>
<li>U+0640 ARABIC TATWEEL: try adding one of: arabic, hanifi-rohingya, manichaean, psalter-pahlavi, sogdian, syriac, old-uyghur, adlam, mandaic</li>
<li>U+0641 ARABIC LETTER FEH: try adding arabic</li>
<li>U+0642 ARABIC LETTER QAF: try adding arabic</li>
<li>U+0643 ARABIC LETTER KAF: try adding arabic</li>
<li>U+0644 ARABIC LETTER LAM: try adding arabic</li>
<li>U+0645 ARABIC LETTER MEEM: try adding arabic</li>
<li>U+0646 ARABIC LETTER NOON: try adding arabic</li>
<li>U+0647 ARABIC LETTER HEH: try adding arabic</li>
<li>U+0648 ARABIC LETTER WAW: try adding arabic</li>
<li>U+0649 ARABIC LETTER ALEF MAKSURA: try adding arabic</li>
<li>U+064A ARABIC LETTER YEH: try adding arabic</li>
<li>U+064B ARABIC FATHATAN: try adding one of: syriac, arabic</li>
<li>U+064C ARABIC DAMMATAN: try adding one of: syriac, arabic</li>
<li>U+064D ARABIC KASRATAN: try adding one of: syriac, arabic</li>
<li>U+064E ARABIC FATHA: try adding one of: syriac, arabic</li>
<li>U+064F ARABIC DAMMA: try adding one of: syriac, arabic</li>
<li>U+0650 ARABIC KASRA: try adding one of: syriac, arabic</li>
<li>U+0651 ARABIC SHADDA: try adding one of: syriac, arabic</li>
<li>U+0652 ARABIC SUKUN: try adding one of: syriac, arabic</li>
<li>U+0653 ARABIC MADDAH ABOVE: try adding one of: syriac, arabic</li>
<li>U+0654 ARABIC HAMZA ABOVE: try adding one of: syriac, arabic</li>
<li>U+0655 ARABIC HAMZA BELOW: try adding one of: syriac, arabic</li>
<li>U+0656 ARABIC SUBSCRIPT ALEF: try adding arabic</li>
<li>U+0658 ARABIC MARK NOON GHUNNA: try adding arabic</li>
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: indic-siyaq-numbers, arabic, hanifi-rohingya, thaana, yezidi, syriac</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: indic-siyaq-numbers, arabic, thaana, yezidi, syriac</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: thaana, nko, syriac, arabic</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: thaana, syriac, arabic</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: thaana, syriac, arabic</li>
<li>U+066D ARABIC FIVE POINTED STAR: try adding arabic</li>
<li>U+066E ARABIC LETTER DOTLESS BEH: try adding arabic</li>
<li>U+066F ARABIC LETTER DOTLESS QAF: try adding arabic</li>
<li>U+0670 ARABIC LETTER SUPERSCRIPT ALEF: try adding one of: syriac, arabic</li>
<li>U+0671 ARABIC LETTER ALEF WASLA: try adding arabic</li>
<li>U+0679 ARABIC LETTER TTEH: try adding arabic</li>
<li>U+067E ARABIC LETTER PEH: try adding arabic</li>
<li>U+0686 ARABIC LETTER TCHEH: try adding arabic</li>
<li>U+0688 ARABIC LETTER DDAL: try adding arabic</li>
<li>U+068E ARABIC LETTER DUL: try adding arabic</li>
<li>U+0691 ARABIC LETTER RREH: try adding arabic</li>
<li>U+0698 ARABIC LETTER JEH: try adding arabic</li>
<li>U+06A1 ARABIC LETTER DOTLESS FEH: try adding arabic</li>
<li>U+06A4 ARABIC LETTER VEH: try adding arabic</li>
<li>U+06A9 ARABIC LETTER KEHEH: try adding arabic</li>
<li>U+06BA ARABIC LETTER NOON GHUNNA: try adding arabic</li>
<li>U+06BE ARABIC LETTER HEH DOACHASHMEE: try adding arabic</li>
<li>U+06C1 ARABIC LETTER HEH GOAL: try adding arabic</li>
<li>U+06C2 ARABIC LETTER HEH GOAL WITH HAMZA ABOVE: try adding arabic</li>
<li>U+06C3 ARABIC LETTER TEH MARBUTA GOAL: try adding arabic</li>
<li>U+06CA ARABIC LETTER WAW WITH TWO DOTS ABOVE: try adding arabic</li>
<li>U+06CC ARABIC LETTER FARSI YEH: try adding arabic</li>
<li>U+06CF ARABIC LETTER WAW WITH DOT ABOVE: try adding arabic</li>
<li>U+06D2 ARABIC LETTER YEH BARREE: try adding arabic</li>
<li>U+06D3 ARABIC LETTER YEH BARREE WITH HAMZA ABOVE: try adding arabic</li>
<li>U+06D4 ARABIC FULL STOP: try adding one of: hanifi-rohingya, yezidi, arabic</li>
<li>U+06D5 ARABIC LETTER AE: try adding arabic</li>
<li>U+06DB ARABIC SMALL HIGH THREE DOTS: try adding arabic</li>
<li>U+06F0 EXTENDED ARABIC-INDIC DIGIT ZERO: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F1 EXTENDED ARABIC-INDIC DIGIT ONE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F2 EXTENDED ARABIC-INDIC DIGIT TWO: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F3 EXTENDED ARABIC-INDIC DIGIT THREE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F4 EXTENDED ARABIC-INDIC DIGIT FOUR: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F5 EXTENDED ARABIC-INDIC DIGIT FIVE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F6 EXTENDED ARABIC-INDIC DIGIT SIX: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F7 EXTENDED ARABIC-INDIC DIGIT SEVEN: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F8 EXTENDED ARABIC-INDIC DIGIT EIGHT: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F9 EXTENDED ARABIC-INDIC DIGIT NINE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+FD3E ORNATE LEFT PARENTHESIS: try adding one of: nko, arabic</li>
<li>U+FD3F ORNATE RIGHT PARENTHESIS: try adding one of: nko, arabic</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* i (U+0069): X=93.0,Y=639.0 (should be at cap-height 640?)

* uni0643.medi: X=250.0,Y=642.0 (should be at cap-height 640?)

* uni0643.medi: X=374.0,Y=642.0 (should be at cap-height 640?)

* uni0643.init: X=250.0,Y=642.0 (should be at cap-height 640?)

* uni0643.init: X=374.0,Y=642.0 (should be at cap-height 640?)

* uni06A9 (U+06A9): X=440.0,Y=642.0 (should be at cap-height 640?)

* uni06A9 (U+06A9): X=564.0,Y=642.0 (should be at cap-height 640?)

* uni06A9.fina: X=440.0,Y=642.0 (should be at cap-height 640?)

* uni06A9.fina: X=564.0,Y=642.0 (should be at cap-height 640?)

* uni06A9.medi: X=250.0,Y=642.0 (should be at cap-height 640?)

* uni06A9.medi: X=374.0,Y=642.0 (should be at cap-height 640?)

* uni06A9.init: X=250.0,Y=642.0 (should be at cap-height 640?)

* uni06A9.init: X=374.0,Y=642.0 (should be at cap-height 640?)

* uni0664 (U+0664): X=262.0,Y=638.0 (should be at cap-height 640?)

* uni0664 (U+0664): X=424.0,Y=638.0 (should be at cap-height 640?)

* uni0668 (U+0668): X=284.0,Y=641.0 (should be at cap-height 640?)

* uni06F8 (U+06F8): X=284.0,Y=641.0 (should be at cap-height 640?)

* quotedblright (U+201D): X=174.0,Y=641.0 (should be at cap-height 640?)

* quotedblright (U+201D): X=211.5,Y=641.0 (should be at cap-height 640?)

* quotedblright (U+201D): X=68.0,Y=641.0 (should be at cap-height 640?)

* quotedblright (U+201D): X=105.5,Y=641.0 (should be at cap-height 640?)

* quoteright (U+2019): X=68.0,Y=641.0 (should be at cap-height 640?)

* quoteright (U+2019): X=105.5,Y=641.0 (should be at cap-height 640?)

* uni0656 (U+0656): X=5.0,Y=-1.0 (should be at baseline 0?)

* uni0656 (U+0656): X=25.0,Y=-1.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID value 'MSTR' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 8 | 12 | 91 | 7 | 118 | 0 | 
| 0% | 0% | 3% | 5% | 39% | 3% | 50% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
