#!/bin/bash
tree -I 'myvenv|venv|__pycache__|__init__.py' --noreport --charset=unicode -o 99_Utility/contents.md

sed -i '' $'s/  / /g' 99_Utility/contents.md 
sed -i '' $'s/--/-/g' 99_Utility/contents.md 
sed -i '' $'s/| /|/g' 99_Utility/contents.md 

sed -i '' $'s/`/╚/g' 99_Utility/contents.md
sed -i '' $'s/|/║/g' 99_Utility/contents.md 
sed -i '' $'s/- /═/g' 99_Utility/contents.md 
sed -i '' $'s/║═/╠═/g' 99_Utility/contents.md 

sed -i '' $'s/ /\&nbsp\;\&nbsp\;/g' 99_Utility/contents.md 

#sed -i '' $'s/`/└/g' 99_Utility/contents.md
#sed -i '' $'s/|/│/g' 99_Utility/contents.md 
#sed -i '' $'s/- /─/g' 99_Utility/contents.md 
#sed -i '' $'s/│─/├─/g' 99_Utility/contents.md 

sed -i '' $'s/$/  /g' 99_Utility/contents.md
