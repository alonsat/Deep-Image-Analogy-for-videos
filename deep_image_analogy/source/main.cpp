#include "DeepAnalogy.cuh"

int main(int argc, char** argv) {

	DeepAnalogy dp;

	if (argc!=15) {

		string model = "C:/Users/User/Downloads/Deep-Image-Analogy-master/Deep-Image-Analogy-master/windows/deep_image_analogy/models/";
	
		string A = "C:/Users/User/Downloads/Deep-Image-Analogy-master/inputs/content224.png";
		string BP = "C:/Users/User/Downloads/Deep-Image-Analogy-master/inputs/content224.png";
		string output = "C:/Users/User/Downloads/Deep-Image-Analogy-master/input/";
		dp.SetModel(model);
		dp.SetA(A);
		dp.SetBPrime(BP);
		dp.SetOutputDir(output);
		dp.SetGPU(0);
		dp.SetRatio(0.5);
		dp.SetBlendWeight(2);
		dp.UsePhotoTransfer(false);
		dp.LoadInputs();
		dp.ComputeAnn();
		
	}
	else{
		dp.SetModel(argv[1]);
		dp.SetA(argv[2]);
		dp.SetBPrime(argv[3]);
		dp.SetOutputDir(argv[4]);
		dp.SetGPU(atoi(argv[5]));
		dp.SetRatio(atof(argv[6]));
		dp.SetRead(atof(argv[9]));
		dp.SetStart(atof(argv[10])); 
		dp.SetSave(atof(argv[11]));
		dp.SetBlendWeight(atoi(argv[7]));
		if (atoi(argv[8]) == 1) {
			dp.UsePhotoTransfer(true);
		}
		else{
			dp.UsePhotoTransfer(false);
		}
		dp.LoadInputs();
		dp.ComputeAnn();
	}



	return 0;
}
