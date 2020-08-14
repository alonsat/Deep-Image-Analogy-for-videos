#ifndef DEEPANALOGY_H
#define DEEPANALOGY_H
#include <string>
#include "opencv2/opencv.hpp"
using namespace std;
class DeepAnalogy
{
public:

	DeepAnalogy();
	~DeepAnalogy();
	
	void SetRatio(float ratio = 0.5);
	void SetBlendWeight(int level = 3);
	void UsePhotoTransfer(bool flag = false);
	void SetModel(string path);
	void SetA(string f_c);
	void SetBPrime(string f_s);
	void SetOutputDir(string f_o);
	void SetGPU(int no);
	void LoadInputs();
	void ComputeAnn();
	void SetRead(int read=0);
	void SetStart(int start=0);
	void SetSave(int save=0);

private:
	float resizeRatio, weightBi;
	int weightLevel, ori_A_rows, ori_A_cols, ori_BP_cols, ori_BP_rows, cur_A_rows, cur_A_cols, cur_BP_rows, cur_BP_cols,doweread,start_layer,save_layer;
	bool photoTransfer;
	string path_model, path_output, file_A, file_BP;
	cv::Mat img_AL, img_BPL, ori_A, ori_BP;

};

#endif