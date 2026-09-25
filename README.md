# Awesome AIGC

**语言:** 中文 | [English](README.en.md)

精选 **视频生成、音频生成、漫画生成** 及相关工具链的开源 Git 仓库。

不是论文全集，也不是闭源产品黄页。只收：有代码或权重、能落地、社区仍在用，或对本工作区（动态漫画 / 讲解视频 / 配音）直接有用的项目。

最近核对：2026-09-25。各分类按 GitHub star 降序；徽章为实时数据，排序以本次核对数为准。

NVIDIA 列：`需要` = 官方本地路径依赖 NVIDIA CUDA；`可选` = CPU / Apple Silicon / AMD 也能跑；`不需要` = 在线 API、CPU 或程序化渲染即可。

最低显存列：该仓库官方本地推理（含官方写明的 offload / 小模型）能跑通的 NVIDIA 显存档，如 `8G` / `12G` / `24G`。不需要英伟达卡填 `—`。第三方 GGUF / 极限压榨不记入此列。

## 目录

- [本工作区已在用](#本工作区已在用)
- [视频生成](#视频生成)
- [低显存与加速](#低显存与加速)
- [口型、数字人、动态人像](#口型数字人动态人像)
- [语音合成 TTS](#语音合成-tts)
- [音乐与音效](#音乐与音效)
- [语音识别](#语音识别)
- [漫画与故事可视化](#漫画与故事可视化)
- [图像生成与角色一致性](#图像生成与角色一致性)
- [工作流与工具链](#工作流与工具链)
- [相关清单](#相关清单)
- [收录原则](#收录原则)

## 本工作区已在用

这些是 `world-peace` 里已经落地的项目，以及它们依赖的上游。新仓库优先对照这一层来选。

| 本地项目 | 在做什么 | NVIDIA | 最低显存 | 上游仓库 |
|---|---|---|---|---|
| `motion-comic` | 日更竖屏动态漫画：分镜、Edge TTS、防抖成片 | 不需要 | — | [ToBeWin/make-motion-comic](https://github.com/ToBeWin/make-motion-comic)、[rany2/edge-tts](https://github.com/rany2/edge-tts) |
| `videoGenrate` | 主题 → 黑底 MG 讲解视频 | 不需要 | — | [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer)、[remotion-dev/remotion](https://github.com/remotion-dev/remotion)、[hexgrad/kokoro](https://github.com/hexgrad/kokoro) |
| `seedance` | 即梦 / Seedance 视频提示词与任务记录 | 不需要 | — | 闭源 API，不收录官方 Git |

## 视频生成

当前开源主力在 Wan / Hunyuan / CogVideoX / LTX。选模型时先看显存和任务（T2V / I2V / 口播），再看生态（ComfyUI 节点是否跟上）。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [hpcaitech/Open-Sora](https://github.com/hpcaitech/Open-Sora) | [![Stars](https://img.shields.io/github/stars/hpcaitech/Open-Sora)](https://github.com/hpcaitech/Open-Sora) | 需要 | 24G | 开源复现 Sora 路线，训练与推理框架完整 | Apache-2.0 |
| [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) | [![Stars](https://img.shields.io/github/stars/Wan-Video/Wan2.2)](https://github.com/Wan-Video/Wan2.2) | 需要 | 24G | 通义万相 2.2，开源视频生成当前主力，T2V / I2V / S2V | Apache-2.0 |
| [Wan-Video/Wan2.1](https://github.com/Wan-Video/Wan2.1) | [![Stars](https://img.shields.io/github/stars/Wan-Video/Wan2.1)](https://github.com/Wan-Video/Wan2.1) | 需要 | 8G | 万相 2.1，生态最熟、LoRA 与节点最多 | Apache-2.0 |
| [zai-org/CogVideo](https://github.com/zai-org/CogVideo) | [![Stars](https://img.shields.io/github/stars/zai-org/CogVideo)](https://github.com/zai-org/CogVideo) | 需要 | 8G | CogVideoX，文图生视频，ComfyUI / LoRA 友好 | Apache-2.0 |
| [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | [![Stars](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanVideo)](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 需要 | 48G | 混元视频一代，质量与中文理解仍有参考价值 | 见仓库 |
| [guoyww/AnimateDiff](https://github.com/guoyww/AnimateDiff) | [![Stars](https://img.shields.io/github/stars/guoyww/AnimateDiff)](https://github.com/guoyww/AnimateDiff) | 需要 | 8G | 给 SD 图生模型加运动模块，角色动画常用 | Apache-2.0 |
| [PKU-YuanGroup/Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan) | [![Stars](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan)](https://github.com/PKU-YuanGroup/Open-Sora-Plan) | 需要 | 24G | 北大元集团开源视频方案，社区资料多 | MIT |
| [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) | [![Stars](https://img.shields.io/github/stars/Lightricks/LTX-Video)](https://github.com/Lightricks/LTX-Video) | 需要 | 8G | LTX 系列，生成快，适合迭代和音画同步实验 | Apache-2.0 |
| [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | [![Stars](https://img.shields.io/github/stars/Lightricks/LTX-2)](https://github.com/Lightricks/LTX-2) | 需要 | 24G | LTX 二代，音画一起生成，官方推理与 LoRA | 见仓库 |
| [Tencent-Hunyuan/HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | [![Stars](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanVideo-1.5)](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | 需要 | 16G | 混元视频 1.5，8.3B 轻量、消费级显卡可跑 | 见仓库 |
| [genmoai/mochi](https://github.com/genmoai/mochi) | [![Stars](https://img.shields.io/github/stars/genmoai/mochi)](https://github.com/genmoai/mochi) | 需要 | 24G | Genmo Mochi，开源视频质量标杆之一 | Apache-2.0 |
| [PKU-YuanGroup/Helios](https://github.com/PKU-YuanGroup/Helios) | [![Stars](https://img.shields.io/github/stars/PKU-YuanGroup/Helios)](https://github.com/PKU-YuanGroup/Helios) | 需要 | 6G | 分钟级长视频、偏实时推理 | Apache-2.0 |

## 低显存与加速

本机 8–16 GB 显存时，先看这类工程仓，再下完整权重。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP) | [![Stars](https://img.shields.io/github/stars/deepbeepmeep/Wan2GP)](https://github.com/deepbeepmeep/Wan2GP) | 可选 | 6G | 低显存一站式：Wan / Hunyuan / LTX / Flux；官方也支持 AMD | 见仓库 |
| [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) | [![Stars](https://img.shields.io/github/stars/kijai/ComfyUI-WanVideoWrapper)](https://github.com/kijai/ComfyUI-WanVideoWrapper) | 需要 | 8G | ComfyUI 里跟进 Wan 新特性最快的封装 | Apache-2.0 |
| [Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) | [![Stars](https://img.shields.io/github/stars/Lightricks/ComfyUI-LTXVideo)](https://github.com/Lightricks/ComfyUI-LTXVideo) | 需要 | 8G | LTX 官方 ComfyUI 工作流 | 见仓库 |
| [ModelTC/LightX2V](https://github.com/ModelTC/LightX2V) | [![Stars](https://img.shields.io/github/stars/ModelTC/LightX2V)](https://github.com/ModelTC/LightX2V) | 需要 | 8G | Wan 系蒸馏、量化、轻量 VAE，偏工程加速 | Apache-2.0 |

## 口型、数字人、动态人像

静态漫画分镜要「说话」或「转头」时用这类，不要和文生视频模型混为一谈。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) | [![Stars](https://img.shields.io/github/stars/KlingAIResearch/LivePortrait)](https://github.com/KlingAIResearch/LivePortrait) | 可选 | 8G | 人像驱动，漫画角色微表情 / 转头常用；官方支持 Apple Silicon | 见仓库 |
| [OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker) | [![Stars](https://img.shields.io/github/stars/OpenTalker/SadTalker)](https://github.com/OpenTalker/SadTalker) | 需要 | 8G | 单图 + 音频驱动说话人脸，资料最多 | 见仓库 |
| [TMElyralab/MuseTalk](https://github.com/TMElyralab/MuseTalk) | [![Stars](https://img.shields.io/github/stars/TMElyralab/MuseTalk)](https://github.com/TMElyralab/MuseTalk) | 需要 | 8G | 实时级口型，适合口播叠加 | 见仓库 |
| [bytedance/LatentSync](https://github.com/bytedance/LatentSync) | [![Stars](https://img.shields.io/github/stars/bytedance/LatentSync)](https://github.com/bytedance/LatentSync) | 需要 | 8G | 字节口型同步，质量稳 | Apache-2.0 |
| [antgroup/echomimic_v2](https://github.com/antgroup/echomimic_v2) | [![Stars](https://img.shields.io/github/stars/antgroup/echomimic_v2)](https://github.com/antgroup/echomimic_v2) | 需要 | 16G | 蚂蚁 EchoMimic V2，半身人像说话 | Apache-2.0 |

## 语音合成 TTS

`motion-comic` 默认走 Edge TTS（零成本在线中文）。要离线、克隆音色、情绪控制时再上本地模型。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | [![Stars](https://img.shields.io/github/stars/RVC-Boss/GPT-SoVITS)](https://github.com/RVC-Boss/GPT-SoVITS) | 可选 | 8G | 一两分钟语料克隆，中文配音事实标准；官方有 CPU / Apple Silicon | MIT |
| [2noise/ChatTTS](https://github.com/2noise/ChatTTS) | [![Stars](https://img.shields.io/github/stars/2noise/ChatTTS)](https://github.com/2noise/ChatTTS) | 可选 | 8G | 对话语气强，适合旁白草稿 | AGPL-3.0 |
| [RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | [![Stars](https://img.shields.io/github/stars/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | 可选 | 8G | RVC 变声，短音频训练角色声线 | MIT |
| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | [![Stars](https://img.shields.io/github/stars/fishaudio/fish-speech)](https://github.com/fishaudio/fish-speech) | 需要 | 8G | Fish Speech / S2，情绪与多语自然度突出 | 见仓库 |
| [index-tts/index-tts](https://github.com/index-tts/index-tts) | [![Stars](https://img.shields.io/github/stars/index-tts/index-tts)](https://github.com/index-tts/index-tts) | 可选 | 8G | IndexTTS，工业级可控零样本 TTS | 见仓库 |
| [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) | [![Stars](https://img.shields.io/github/stars/QwenAudio/CosyVoice)](https://github.com/QwenAudio/CosyVoice) | 可选 | 8G | CosyVoice 3，多语零样本克隆，中文方言强 | Apache-2.0 |
| [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) | [![Stars](https://img.shields.io/github/stars/SWivid/F5-TTS)](https://github.com/SWivid/F5-TTS) | 可选 | 8G | Flow Matching TTS；官方支持 NVIDIA / AMD / Intel / Apple | MIT |
| [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | [![Stars](https://img.shields.io/github/stars/QwenLM/Qwen3-TTS)](https://github.com/QwenLM/Qwen3-TTS) | 可选 | 8G | 通义 Qwen3-TTS，流式、音色设计与克隆 | Apache-2.0 |
| [rany2/edge-tts](https://github.com/rany2/edge-tts) | [![Stars](https://img.shields.io/github/stars/rany2/edge-tts)](https://github.com/rany2/edge-tts) | 不需要 | — | 微软 Edge 在线神经语音，本仓库动态漫画默认路线 | 见仓库 |
| [SparkAudio/Spark-TTS](https://github.com/SparkAudio/Spark-TTS) | [![Stars](https://img.shields.io/github/stars/SparkAudio/Spark-TTS)](https://github.com/SparkAudio/Spark-TTS) | 可选 | 8G | Spark-TTS，推理简单、中英可用 | Apache-2.0 |
| [hexgrad/kokoro](https://github.com/hexgrad/kokoro) | [![Stars](https://img.shields.io/github/stars/hexgrad/kokoro)](https://github.com/hexgrad/kokoro) | 不需要 | — | 82M 小模型，讲解视频英文配音轻量方案；CPU / Apple Silicon 可跑 | Apache-2.0 |
| [fishaudio/Bert-VITS2](https://github.com/fishaudio/Bert-VITS2) | [![Stars](https://img.shields.io/github/stars/fishaudio/Bert-VITS2)](https://github.com/fishaudio/Bert-VITS2) | 可选 | 8G | 中文歌声 / 角色感 TTS，仍有大量音色 | AGPL-3.0 |

## 音乐与音效

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) | [![Stars](https://img.shields.io/github/stars/facebookresearch/audiocraft)](https://github.com/facebookresearch/audiocraft) | 可选 | 8G | MusicGen / AudioGen，文生音乐与音效 | MIT |
| [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | [![Stars](https://img.shields.io/github/stars/ace-step/ACE-Step-1.5)](https://github.com/ace-step/ACE-Step-1.5) | 可选 | 8G | ACE-Step 1.5，本地音乐生成当前主力 | MIT |
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | [![Stars](https://img.shields.io/github/stars/multimodal-art-projection/YuE)](https://github.com/multimodal-art-projection/YuE) | 可选 | 24G | YuE，开源歌声与带词音乐生成 | Apache-2.0 |
| [ace-step/ACE-Step](https://github.com/ace-step/ACE-Step) | [![Stars](https://img.shields.io/github/stars/ace-step/ACE-Step)](https://github.com/ace-step/ACE-Step) | 可选 | 8G | 开源音乐基础模型，生成速度快 | Apache-2.0 |
| [Stability-AI/stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) | [![Stars](https://img.shields.io/github/stars/Stability-AI/stable-audio-tools)](https://github.com/Stability-AI/stable-audio-tools) | 可选 | 12G | Stable Audio 训练与推理工具 | MIT |

## 语音识别

配字幕、对时间轴、从成片反抽台词时用。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [openai/whisper](https://github.com/openai/whisper) | [![Stars](https://img.shields.io/github/stars/openai/whisper)](https://github.com/openai/whisper) | 不需要 | — | 开源 ASR 事实标准，本地转写稳；CPU 可跑 | MIT |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | [![Stars](https://img.shields.io/github/stars/ggml-org/whisper.cpp)](https://github.com/ggml-org/whisper.cpp) | 不需要 | — | Whisper 的 C++ 移植，CPU / 苹果机本地转写 | MIT |

## 漫画与故事可视化

分两类：研究向「连续角色出格」、产品向「小说 / 剧本 → 分页漫画」。动态漫画防抖成片见本工作区 `motion-comic`。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [zyddnys/manga-image-translator](https://github.com/zyddnys/manga-image-translator) | [![Stars](https://img.shields.io/github/stars/zyddnys/manga-image-translator)](https://github.com/zyddnys/manga-image-translator) | 可选 | 8G | 漫画图内文字检测、翻译、重排字 | GPL-3.0 |
| [HVision-NKU/StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | [![Stars](https://img.shields.io/github/stars/HVision-NKU/StoryDiffusion)](https://github.com/HVision-NKU/StoryDiffusion) | 需要 | 12G | 长序列角色一致性，连环画 / 分镜常用 | Apache-2.0 |
| [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | [![Stars](https://img.shields.io/github/stars/gnipbao/story-to-handdrawn-video)](https://github.com/gnipbao/story-to-handdrawn-video) | 不需要 | — | 中文故事或有序图 → 手绘日记漫画静音成片 | MIT |
| [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | [![Stars](https://img.shields.io/github/stars/Vincentwei1021/anything2explainer)](https://github.com/Vincentwei1021/anything2explainer) | 不需要 | — | 主题 → 代码绘制讲解视频（非绘本，但是叙事成片） | 见仓库 |
| [jbilcke-hf/ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) | [![Stars](https://img.shields.io/github/stars/jbilcke-hf/ai-comic-factory)](https://github.com/jbilcke-hf/ai-comic-factory) | 需要 | 12G | LLM + SDXL 出漫画格，Hugging Face 生态 | Apache-2.0 |
| [jianzongwu/DiffSensei](https://github.com/jianzongwu/DiffSensei) | [![Stars](https://img.shields.io/github/stars/jianzongwu/DiffSensei)](https://github.com/jianzongwu/DiffSensei) | 需要 | 12G | CVPR 2025，可控黑白漫画格、多角色 | 见仓库 |
| [ToBeWin/make-motion-comic](https://github.com/ToBeWin/make-motion-comic) | [![Stars](https://img.shields.io/github/stars/ToBeWin/make-motion-comic)](https://github.com/ToBeWin/make-motion-comic) | 不需要 | — | 关键帧 + 中文 TTS + FFmpeg 防抖，动态漫画引擎 | MIT |

## 图像生成与角色一致性

漫画和分镜先稳住脸与服装，再谈视频。Flux / Qwen-Image 出静帧，InstantID / PuLID / IP-Adapter 锁身份。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [lllyasviel/ControlNet](https://github.com/lllyasviel/ControlNet) | [![Stars](https://img.shields.io/github/stars/lllyasviel/ControlNet)](https://github.com/lllyasviel/ControlNet) | 需要 | 8G | 姿态、线稿、深度控图，分镜构图必备 | Apache-2.0 |
| [black-forest-labs/flux](https://github.com/black-forest-labs/flux) | [![Stars](https://img.shields.io/github/stars/black-forest-labs/flux)](https://github.com/black-forest-labs/flux) | 需要 | 12G | FLUX.1 官方推理，静帧画质主力 | Apache-2.0 |
| [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | [![Stars](https://img.shields.io/github/stars/Tencent-Hunyuan/Hunyuan3D-2)](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | 需要 | 6G | 图生 3D 资产，后续做可转向角色 | 见仓库 |
| [instantX-research/InstantID](https://github.com/instantX-research/InstantID) | [![Stars](https://img.shields.io/github/stars/instantX-research/InstantID)](https://github.com/instantX-research/InstantID) | 需要 | 12G | 单张参考图锁人脸，零样本 | Apache-2.0 |
| [QwenLM/Qwen-Image](https://github.com/QwenLM/Qwen-Image) | [![Stars](https://img.shields.io/github/stars/QwenLM/Qwen-Image)](https://github.com/QwenLM/Qwen-Image) | 需要 | 16G | 通义图像，复杂文字渲染和精修强 | Apache-2.0 |
| [tencent-ailab/IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | [![Stars](https://img.shields.io/github/stars/tencent-ailab/IP-Adapter)](https://github.com/tencent-ailab/IP-Adapter) | 需要 | 8G | 图提示适配器，风格 / 主体迁移底座 | Apache-2.0 |
| [ToTheBeginning/PuLID](https://github.com/ToTheBeginning/PuLID) | [![Stars](https://img.shields.io/github/stars/ToTheBeginning/PuLID)](https://github.com/ToTheBeginning/PuLID) | 需要 | 12G | 身份定制，SDXL / FLUX 都有权重 | Apache-2.0 |
| [black-forest-labs/flux2](https://github.com/black-forest-labs/flux2) | [![Stars](https://img.shields.io/github/stars/black-forest-labs/flux2)](https://github.com/black-forest-labs/flux2) | 需要 | 16G | FLUX.2 官方推理 | Apache-2.0 |
| [bytedance/DreamO](https://github.com/bytedance/DreamO) | [![Stars](https://img.shields.io/github/stars/bytedance/DreamO)](https://github.com/bytedance/DreamO) | 需要 | 24G | 统一图像定制：ID / IP / 试穿 / 风格 | Apache-2.0 |

## 工作流与工具链

模型换得快，节点图和训练脚本更耐用。

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 | 许可 |
|---|---|---|---|---|---|
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | [![Stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI)](https://github.com/Comfy-Org/ComfyUI) | 可选 | 8G | 节点式扩散工作流；官方支持 NVIDIA / AMD / Intel / Apple | GPL-3.0 |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | [![Stars](https://img.shields.io/github/stars/remotion-dev/remotion)](https://github.com/remotion-dev/remotion) | 不需要 | — | React 程序化视频，讲解片时间轴 | 见仓库 |
| [huggingface/diffusers](https://github.com/huggingface/diffusers) | [![Stars](https://img.shields.io/github/stars/huggingface/diffusers)](https://github.com/huggingface/diffusers) | 可选 | 8G | PyTorch 扩散推理标准库 | Apache-2.0 |
| [Comfy-Org/ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) | [![Stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI-Manager)](https://github.com/Comfy-Org/ComfyUI-Manager) | 可选 | — | ComfyUI 节点安装与版本管理 | GPL-3.0 |
| [lllyasviel/stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) | [![Stars](https://img.shields.io/github/stars/lllyasviel/stable-diffusion-webui-forge)](https://github.com/lllyasviel/stable-diffusion-webui-forge) | 需要 | 8G | Forge，WebUI 路线里更省显存 | AGPL-3.0 |
| [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts) | [![Stars](https://img.shields.io/github/stars/kohya-ss/sd-scripts)](https://github.com/kohya-ss/sd-scripts) | 需要 | 8G | LoRA / 微调脚本，角色画风训练常用 | Apache-2.0 |

## 相关清单

| 项目 | ★ | NVIDIA | 最低显存 | 一句话 |
|---|---|---|---|---|
| [mantoufan/awesome-text-to-video](https://github.com/mantoufan/awesome-text-to-video) | [![Stars](https://img.shields.io/github/stars/mantoufan/awesome-text-to-video)](https://github.com/mantoufan/awesome-text-to-video) | — | — | 文生视频模型与商业产品对照，更新勤 |

## 收录原则

1. **能跑**：有仓库、有推理或训练代码；纯论文主页不进主表。
2. **能选**：写清许可。`AGPL-3.0`、未声明、商用另议的，标注在许可列，避免误用。
3. **能接**：优先收能接到动态漫画、讲解视频、配音、角色一致性管线的项目。
4. **少而准**：同类只留当前更好用的 1–3 个，旧版降到备注或删除。

新增条目见 [CONTRIBUTING.md](CONTRIBUTING.md)。中英两份 README 需同步更新。
