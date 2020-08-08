#!/bin/sh

source=deep_image_analogy/source

nvcc $source/*.cpp $source/*.cu -o demo \
	-std=c++11 \
	-I./include \
	-L./build/lib \
	-L/usr/local/lib \
	-lopencv_core \
	-lopencv_highgui \
	-lopencv_imgproc \
	-lopencv_imgcodecs \
	-lboost_system \
	-lcublas \
	-lcaffe \
	-lglog
