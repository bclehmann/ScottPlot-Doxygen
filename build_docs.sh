#!/bin/bash

pushd ScottPlot
git pull
popd

git add ./ScottPlot
doxygen ./Doxyfile

git add ./outdocs

git commit -m "Version bump"

git push


