# 文本检测


## 文件夹概述
- request.py : 用于调用数学院大模型，这是直接使用开源的Qwen2-72B-int4
- documents : 俩篇文本检测的文章
- DetectGPT/ FastDetectGPT : code对应documents文章
- 运行推荐使用gpt2替代 :

        python FastDetectGPT/scripts/local_infer.py  --reference_model_name gpt2 

## 调研
### 参考文献

1. **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature** https://arxiv.org/pdf/2301.11305
Code : https://github.com/eric-mitchell/detect-gpt

2. **Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense** https://arxiv.org/pdf/2303.13408
Code : https://github.com/martiansideofthemoon/ai-detection-paraphrases

3. **A Watermark for Large Language Models** https://arxiv.org/pdf/2301.10226
On the Reliability of Watermarks for Large Language Models https://arxiv.org/pdf/2306.04634
Code: https://github.com/jwkirchenbauer/lm-watermarking

4. **Can AI-Generated Text be Reliably Detected?**: https://arxiv.org/pdf/2303.11156
Code: https://github.com/vinusankars/Reliability-of-AI-text-detectors

5. **RADAR: Robust AI-Text Detection via Adversarial Learning**
https://arxiv.org/pdf/2307.03838
Code: https://github.com/IBM/RADAR

6. **Kaggle AI Text Detection Competition First Prize Blog**
https://www.kaggle.com/competitions/llm-detect-ai-generated-text/discussion/473295
Code: https://github.com/rbiswasfc/llm-detect-ai

---
 1/11/2024更新 补充

7. **Ghostbuster: Detecting Text Ghostwritten by Large Language Models**
文章: http://arxiv.org/abs/2305.15047
代码: https://github.com/vivek3141/ghostbuster
论文分析：https://blog.csdn.net/xieyan0811/article/details/134743114
作者: Vivek Verma，Eve Fleisig，Nicholas Tomlin，Dan Klein
日期: 2023-11-13


8. **The Science of Detecting LLM-Generated Texts**
论文连接：https://drive.google.com/file/d/1U8oQNU4f-1c4hJG9vdFuV4xfa10mrKXC/view

9. **Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature**
论文连接：https://doi.org/10.48550/arXiv.2310.05130
The code and data are released at https://github.com/baoguangsheng/fast-detect-gpt

10. **检测局部文本的 AI 润色或改写：Spotting AI's Touch: Identifying LLM-Paraphrased Spans in Text**
论文连接：https://doi.org/10.48550/arXiv.2405.12689

11. **AI-Generated Text Detection and Classification Based on BERT Deep Learning Algorithm**
论文连接：https://doi.org/10.48550/arXiv.2405.16422


二 应用

-----国外：

1 GPTzero https://gptzero.me/
blog:
https://support.gptzero.me/hc/en-us/articles/15130070230551-How-do-I-interpret-burstiness-or-perplexity
https://gptzero.me/technology

2 Content at scale : https://brandwell.ai/ai-content-detector/
blog: https://brandwell.ai/blog/how-to-remove-ai-detection/#bestaidetectortools

3 Copyleaks : https://copyleaks.com/ai-content-detector
Blog: https://copyleaks.com/blog/how-does-ai-detection-work

4 originality.ai https://originality.ai/ai-checker
Blog : https://originality.ai/blog/how-does-ai-content-detection-work

5 GPT-2 Output Detector Demo https://openai-openai-detector.hf.space/

-----国内：(均未找到技术报告)
1知网/读者服务/工具应用/个人AIGC检测https://www-cnki-net-443.webvpn.las.ac.cn/new/
2 维普论文检测系统 https://vpcs.fanyu.com/aigcUpload
3 Master AI https://pass.checkttup.com/

三 新闻报道
AI-text detection tools are really easy to fool（twitter上广为流传）https://www.technologyreview.com/2023/07/07/1075982/ai-text-detection-tools-are-really-easy-to-fool/?utm_source=dlvr.it&utm_medium=twitter

四 对抗ai文本检测的工具
1 AIPRM : https://www.aiprm.com/
2 stealthwriter https://stealthwriter.ai/