mkdir temp
cd temp
npm create vite@latest .
cd ..
mv temp/* temp/.* . 2>/dev/null
rm -rf temp
