# Awesome AIGC

**Language:** [中文](README.md) | English

Curated open-source Git repos for **video generation, audio generation, comic generation**, and the tooling around them.

This is not a paper index and not a closed-source product directory. We only list projects that have code or weights, that you can actually run, that the community still uses, or that plug directly into this workspace (motion comics / explainer videos / voiceover).

Last checked: 2026-09-24. Tables in each section are sorted by GitHub stars (high → low). Badges stay live; ranking follows this snapshot.

NVIDIA column: `required` = official local path needs NVIDIA CUDA; `optional` = CPU / Apple Silicon / AMD also work; `no` = cloud API, CPU, or CPU rendering.

VRAM column: minimum NVIDIA VRAM for this repo's official local inference path (including official offload / small variants), e.g. `8G` / `12G` / `24G`. Use `—` when no NVIDIA GPU is required. Third-party GGUF / extreme offload paths are not counted.

## Contents

- [Already in this workspace](#already-in-this-workspace)
- [Video generation](#video-generation)
- [Low VRAM and acceleration](#low-vram-and-acceleration)
- [Lip-sync, digital humans, animated portraits](#lip-sync-digital-humans-animated-portraits)
- [Speech synthesis (TTS)](#speech-synthesis-tts)
- [Music and sound effects](#music-and-sound-effects)
- [Speech recognition](#speech-recognition)
- [Comics and story visualization](#comics-and-story-visualization)
- [Image generation and character consistency](#image-generation-and-character-consistency)
- [Workflows and tooling](#workflows-and-tooling)
- [Related lists](#related-lists)
- [Inclusion rules](#inclusion-rules)

## Already in this workspace

These are projects already running in `world-peace`, plus the upstream repos they depend on. Prefer new candidates that map to this layer.

| Local project | What it does | NVIDIA | VRAM | Upstream |
|---|---|---|---|---|
| `motion-comic` | Daily vertical motion comics: storyboard, Edge TTS, stabilized video | no | — | [ToBeWin/make-motion-comic](https://github.com/ToBeWin/make-motion-comic), [rany2/edge-tts](https://github.com/rany2/edge-tts) |
| `videoGenrate` | Topic → black-background motion-graphics explainer | no | — | [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer), [remotion-dev/remotion](https://github.com/remotion-dev/remotion), [hexgrad/kokoro](https://github.com/hexgrad/kokoro) |
| `seedance` | Jimeng / Seedance video prompts and task logs | no | — | Closed-source API; no official Git listed |

## Video generation

The current open-source core is Wan / Hunyuan / CogVideoX / LTX. Pick by VRAM and task (T2V / I2V / talking-head) first, then by ecosystem (whether ComfyUI nodes have caught up).

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [hpcaitech/Open-Sora](https://github.com/hpcaitech/Open-Sora) | [![Stars](https://img.shields.io/github/stars/hpcaitech/Open-Sora)](https://github.com/hpcaitech/Open-Sora) | required | 24G | Open Sora-style stack with a full train + inference framework | Apache-2.0 |
| [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) | [![Stars](https://img.shields.io/github/stars/Wan-Video/Wan2.2)](https://github.com/Wan-Video/Wan2.2) | required | 24G | Tongyi Wanxiang 2.2, current open video-gen workhorse, T2V / I2V / S2V | Apache-2.0 |
| [Wan-Video/Wan2.1](https://github.com/Wan-Video/Wan2.1) | [![Stars](https://img.shields.io/github/stars/Wan-Video/Wan2.1)](https://github.com/Wan-Video/Wan2.1) | required | 8G | Wan 2.1, most mature ecosystem, most LoRAs and nodes | Apache-2.0 |
| [zai-org/CogVideo](https://github.com/zai-org/CogVideo) | [![Stars](https://img.shields.io/github/stars/zai-org/CogVideo)](https://github.com/zai-org/CogVideo) | required | 8G | CogVideoX, text/image-to-video, ComfyUI / LoRA friendly | Apache-2.0 |
| [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | [![Stars](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanVideo)](https://github.com/Tencent-Hunyuan/HunyuanVideo) | required | 48G | Hunyuan Video v1, still useful for quality and Chinese understanding | see repo |
| [guoyww/AnimateDiff](https://github.com/guoyww/AnimateDiff) | [![Stars](https://img.shields.io/github/stars/guoyww/AnimateDiff)](https://github.com/guoyww/AnimateDiff) | required | 8G | Motion modules for SD image models; common for character animation | Apache-2.0 |
| [PKU-YuanGroup/Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan) | [![Stars](https://img.shields.io/github/stars/PKU-YuanGroup/Open-Sora-Plan)](https://github.com/PKU-YuanGroup/Open-Sora-Plan) | required | 24G | PKU Yuan Group video stack with lots of community material | MIT |
| [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) | [![Stars](https://img.shields.io/github/stars/Lightricks/LTX-Video)](https://github.com/Lightricks/LTX-Video) | required | 8G | LTX series, fast generation, good for iteration and A/V sync | Apache-2.0 |
| [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | [![Stars](https://img.shields.io/github/stars/Lightricks/LTX-2)](https://github.com/Lightricks/LTX-2) | required | 24G | LTX-2 official inference and LoRA; joint audio-video | see repo |
| [Tencent-Hunyuan/HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | [![Stars](https://img.shields.io/github/stars/Tencent-Hunyuan/HunyuanVideo-1.5)](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | required | 16G | Hunyuan Video 1.5, 8.3B lightweight, runs on consumer GPUs | see repo |
| [genmoai/mochi](https://github.com/genmoai/mochi) | [![Stars](https://img.shields.io/github/stars/genmoai/mochi)](https://github.com/genmoai/mochi) | required | 24G | Genmo Mochi, a quality benchmark among open video models | Apache-2.0 |
| [PKU-YuanGroup/Helios](https://github.com/PKU-YuanGroup/Helios) | [![Stars](https://img.shields.io/github/stars/PKU-YuanGroup/Helios)](https://github.com/PKU-YuanGroup/Helios) | required | 6G | Minute-long video, leaning real-time inference | Apache-2.0 |

## Low VRAM and acceleration

On 8–16 GB VRAM, start with these engineering repos before downloading full weights.

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP) | [![Stars](https://img.shields.io/github/stars/deepbeepmeep/Wan2GP)](https://github.com/deepbeepmeep/Wan2GP) | optional | 6G | One-stop low-VRAM: Wan / Hunyuan / LTX / Flux; official AMD support | see repo |
| [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) | [![Stars](https://img.shields.io/github/stars/kijai/ComfyUI-WanVideoWrapper)](https://github.com/kijai/ComfyUI-WanVideoWrapper) | required | 8G | Fastest ComfyUI wrapper tracking new Wan features | Apache-2.0 |
| [Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) | [![Stars](https://img.shields.io/github/stars/Lightricks/ComfyUI-LTXVideo)](https://github.com/Lightricks/ComfyUI-LTXVideo) | required | 8G | Official LTX ComfyUI workflows | see repo |
| [ModelTC/LightX2V](https://github.com/ModelTC/LightX2V) | [![Stars](https://img.shields.io/github/stars/ModelTC/LightX2V)](https://github.com/ModelTC/LightX2V) | required | 8G | Wan-family distillation, quant, light VAE; engineering speedups | Apache-2.0 |

## Lip-sync, digital humans, animated portraits

Use these when a still comic frame needs to talk or turn its head. Do not treat them as text-to-video models.

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) | [![Stars](https://img.shields.io/github/stars/KlingAIResearch/LivePortrait)](https://github.com/KlingAIResearch/LivePortrait) | optional | 8G | Portrait driving; micro-expressions / head turns; official Apple Silicon | see repo |
| [OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker) | [![Stars](https://img.shields.io/github/stars/OpenTalker/SadTalker)](https://github.com/OpenTalker/SadTalker) | required | 8G | Single image + audio talking face; most tutorials | see repo |
| [TMElyralab/MuseTalk](https://github.com/TMElyralab/MuseTalk) | [![Stars](https://img.shields.io/github/stars/TMElyralab/MuseTalk)](https://github.com/TMElyralab/MuseTalk) | required | 8G | Near-real-time lips; good for talking-head overlay | see repo |
| [bytedance/LatentSync](https://github.com/bytedance/LatentSync) | [![Stars](https://img.shields.io/github/stars/bytedance/LatentSync)](https://github.com/bytedance/LatentSync) | required | 8G | ByteDance lip-sync with stable quality | Apache-2.0 |
| [antgroup/echomimic_v2](https://github.com/antgroup/echomimic_v2) | [![Stars](https://img.shields.io/github/stars/antgroup/echomimic_v2)](https://github.com/antgroup/echomimic_v2) | required | 16G | EchoMimic V2, striking half-body talking portraits | Apache-2.0 |

## Speech synthesis (TTS)

`motion-comic` defaults to Edge TTS (free online Chinese). Switch to a local model when you need offline use, voice cloning, or emotion control.

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | [![Stars](https://img.shields.io/github/stars/RVC-Boss/GPT-SoVITS)](https://github.com/RVC-Boss/GPT-SoVITS) | optional | 8G | Clone from 1–2 minutes of audio; official CPU / Apple Silicon | MIT |
| [2noise/ChatTTS](https://github.com/2noise/ChatTTS) | [![Stars](https://img.shields.io/github/stars/2noise/ChatTTS)](https://github.com/2noise/ChatTTS) | optional | 8G | Strong conversational tone; good for narration drafts | AGPL-3.0 |
| [RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | [![Stars](https://img.shields.io/github/stars/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | optional | 8G | RVC voice conversion; train a character timbre from short audio | MIT |
| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | [![Stars](https://img.shields.io/github/stars/fishaudio/fish-speech)](https://github.com/fishaudio/fish-speech) | required | 8G | Fish Speech / S2; emotion and multilingual naturalness | see repo |
| [index-tts/index-tts](https://github.com/index-tts/index-tts) | [![Stars](https://img.shields.io/github/stars/index-tts/index-tts)](https://github.com/index-tts/index-tts) | optional | 8G | IndexTTS, industrial controllable zero-shot TTS | see repo |
| [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) | [![Stars](https://img.shields.io/github/stars/QwenAudio/CosyVoice)](https://github.com/QwenAudio/CosyVoice) | optional | 8G | CosyVoice 3, multilingual zero-shot clone, strong Chinese dialects | Apache-2.0 |
| [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) | [![Stars](https://img.shields.io/github/stars/SWivid/F5-TTS)](https://github.com/SWivid/F5-TTS) | optional | 8G | Flow Matching TTS; official NVIDIA / AMD / Intel / Apple | MIT |
| [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | [![Stars](https://img.shields.io/github/stars/QwenLM/Qwen3-TTS)](https://github.com/QwenLM/Qwen3-TTS) | optional | 8G | Qwen3-TTS, streaming speech, voice design and cloning | Apache-2.0 |
| [rany2/edge-tts](https://github.com/rany2/edge-tts) | [![Stars](https://img.shields.io/github/stars/rany2/edge-tts)](https://github.com/rany2/edge-tts) | no | — | Microsoft Edge online neural voices; default for motion comics here | see repo |
| [SparkAudio/Spark-TTS](https://github.com/SparkAudio/Spark-TTS) | [![Stars](https://img.shields.io/github/stars/SparkAudio/Spark-TTS)](https://github.com/SparkAudio/Spark-TTS) | optional | 8G | Spark-TTS, simple inference, Chinese + English | Apache-2.0 |
| [hexgrad/kokoro](https://github.com/hexgrad/kokoro) | [![Stars](https://img.shields.io/github/stars/hexgrad/kokoro)](https://github.com/hexgrad/kokoro) | no | — | 82M small model; CPU / Apple Silicon English voiceover | Apache-2.0 |
| [fishaudio/Bert-VITS2](https://github.com/fishaudio/Bert-VITS2) | [![Stars](https://img.shields.io/github/stars/fishaudio/Bert-VITS2)](https://github.com/fishaudio/Bert-VITS2) | optional | 8G | Chinese singing / character TTS; still many voices | AGPL-3.0 |

## Music and sound effects

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) | [![Stars](https://img.shields.io/github/stars/facebookresearch/audiocraft)](https://github.com/facebookresearch/audiocraft) | optional | 8G | MusicGen / AudioGen, text-to-music and SFX | MIT |
| [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | [![Stars](https://img.shields.io/github/stars/ace-step/ACE-Step-1.5)](https://github.com/ace-step/ACE-Step-1.5) | optional | 8G | ACE-Step 1.5, current local music-generation workhorse | MIT |
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | [![Stars](https://img.shields.io/github/stars/multimodal-art-projection/YuE)](https://github.com/multimodal-art-projection/YuE) | optional | 24G | YuE, open singing / lyric-conditioned music generation | Apache-2.0 |
| [ace-step/ACE-Step](https://github.com/ace-step/ACE-Step) | [![Stars](https://img.shields.io/github/stars/ace-step/ACE-Step)](https://github.com/ace-step/ACE-Step) | optional | 8G | Open music foundation model, fast generation | Apache-2.0 |
| [Stability-AI/stable-audio-tools](https://github.com/Stability-AI/stable-audio-tools) | [![Stars](https://img.shields.io/github/stars/Stability-AI/stable-audio-tools)](https://github.com/Stability-AI/stable-audio-tools) | optional | 12G | Stable Audio train + inference tools | MIT |

## Speech recognition

Use this for subtitles, timeline alignment, and pulling dialogue back from a finished video.

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [openai/whisper](https://github.com/openai/whisper) | [![Stars](https://img.shields.io/github/stars/openai/whisper)](https://github.com/openai/whisper) | no | — | De facto open ASR; reliable local transcription on CPU | MIT |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | [![Stars](https://img.shields.io/github/stars/ggml-org/whisper.cpp)](https://github.com/ggml-org/whisper.cpp) | no | — | C++ port of Whisper; local transcription on CPU / Apple | MIT |

## Comics and story visualization

Two tracks: research-style continuous character panels, and product-style novel / script → paginated comics. For motion-comic stabilization, see `motion-comic` in this workspace.

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [zyddnys/manga-image-translator](https://github.com/zyddnys/manga-image-translator) | [![Stars](https://img.shields.io/github/stars/zyddnys/manga-image-translator)](https://github.com/zyddnys/manga-image-translator) | optional | 8G | In-image text detect, translate, and re-typeset | GPL-3.0 |
| [HVision-NKU/StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | [![Stars](https://img.shields.io/github/stars/HVision-NKU/StoryDiffusion)](https://github.com/HVision-NKU/StoryDiffusion) | required | 12G | Long-sequence character consistency; comics / storyboards | Apache-2.0 |
| [gnipbao/story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | [![Stars](https://img.shields.io/github/stars/gnipbao/story-to-handdrawn-video)](https://github.com/gnipbao/story-to-handdrawn-video) | no | — | Chinese story or ordered images → silent hand-drawn diary-comic video | MIT |
| [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | [![Stars](https://img.shields.io/github/stars/Vincentwei1021/anything2explainer)](https://github.com/Vincentwei1021/anything2explainer) | no | — | Topic → code-drawn explainer video (narrative video, not a picture book) | see repo |
| [jbilcke-hf/ai-comic-factory](https://github.com/jbilcke-hf/ai-comic-factory) | [![Stars](https://img.shields.io/github/stars/jbilcke-hf/ai-comic-factory)](https://github.com/jbilcke-hf/ai-comic-factory) | required | 12G | LLM + SDXL comic panels in the Hugging Face ecosystem | Apache-2.0 |
| [jianzongwu/DiffSensei](https://github.com/jianzongwu/DiffSensei) | [![Stars](https://img.shields.io/github/stars/jianzongwu/DiffSensei)](https://github.com/jianzongwu/DiffSensei) | required | 12G | CVPR 2025, controllable B&W comic panels, multi-character | see repo |
| [ToBeWin/make-motion-comic](https://github.com/ToBeWin/make-motion-comic) | [![Stars](https://img.shields.io/github/stars/ToBeWin/make-motion-comic)](https://github.com/ToBeWin/make-motion-comic) | no | — | Keyframes + Chinese TTS + FFmpeg stabilization; motion-comic engine | MIT |

## Image generation and character consistency

Lock face and costume on stills before you move to video. Flux / Qwen-Image for frames; InstantID / PuLID / IP-Adapter for identity.

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [lllyasviel/ControlNet](https://github.com/lllyasviel/ControlNet) | [![Stars](https://img.shields.io/github/stars/lllyasviel/ControlNet)](https://github.com/lllyasviel/ControlNet) | required | 8G | Pose, lineart, depth control — essential for storyboard composition | Apache-2.0 |
| [black-forest-labs/flux](https://github.com/black-forest-labs/flux) | [![Stars](https://img.shields.io/github/stars/black-forest-labs/flux)](https://github.com/black-forest-labs/flux) | required | 12G | Official FLUX.1 inference; still-frame quality workhorse | Apache-2.0 |
| [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | [![Stars](https://img.shields.io/github/stars/Tencent-Hunyuan/Hunyuan3D-2)](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | required | 6G | Image-to-3D assets, then turnable characters | see repo |
| [instantX-research/InstantID](https://github.com/instantX-research/InstantID) | [![Stars](https://img.shields.io/github/stars/instantX-research/InstantID)](https://github.com/instantX-research/InstantID) | required | 12G | Lock a face from one reference, zero-shot | Apache-2.0 |
| [QwenLM/Qwen-Image](https://github.com/QwenLM/Qwen-Image) | [![Stars](https://img.shields.io/github/stars/QwenLM/Qwen-Image)](https://github.com/QwenLM/Qwen-Image) | required | 16G | Tongyi Image; strong complex text rendering and edits | Apache-2.0 |
| [tencent-ailab/IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | [![Stars](https://img.shields.io/github/stars/tencent-ailab/IP-Adapter)](https://github.com/tencent-ailab/IP-Adapter) | required | 8G | Image-prompt adapter; style / subject transfer base | Apache-2.0 |
| [ToTheBeginning/PuLID](https://github.com/ToTheBeginning/PuLID) | [![Stars](https://img.shields.io/github/stars/ToTheBeginning/PuLID)](https://github.com/ToTheBeginning/PuLID) | required | 12G | Identity customization; weights for SDXL / FLUX | Apache-2.0 |
| [black-forest-labs/flux2](https://github.com/black-forest-labs/flux2) | [![Stars](https://img.shields.io/github/stars/black-forest-labs/flux2)](https://github.com/black-forest-labs/flux2) | required | 16G | Official FLUX.2 inference | Apache-2.0 |
| [bytedance/DreamO](https://github.com/bytedance/DreamO) | [![Stars](https://img.shields.io/github/stars/bytedance/DreamO)](https://github.com/bytedance/DreamO) | required | 24G | Unified image customization: ID / IP / try-on / style | Apache-2.0 |

## Workflows and tooling

Models change fast. Node graphs and training scripts last longer.

| Project | ★ | NVIDIA | VRAM | One-liner | License |
|---|---|---|---|---|---|
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | [![Stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI)](https://github.com/Comfy-Org/ComfyUI) | optional | 8G | Node-based diffusion; official NVIDIA / AMD / Intel / Apple | GPL-3.0 |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | [![Stars](https://img.shields.io/github/stars/remotion-dev/remotion)](https://github.com/remotion-dev/remotion) | no | — | React programmatic video; explainer timelines | see repo |
| [huggingface/diffusers](https://github.com/huggingface/diffusers) | [![Stars](https://img.shields.io/github/stars/huggingface/diffusers)](https://github.com/huggingface/diffusers) | optional | 8G | Standard PyTorch diffusion inference library | Apache-2.0 |
| [Comfy-Org/ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) | [![Stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI-Manager)](https://github.com/Comfy-Org/ComfyUI-Manager) | optional | — | Install and manage ComfyUI custom nodes | GPL-3.0 |
| [lllyasviel/stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) | [![Stars](https://img.shields.io/github/stars/lllyasviel/stable-diffusion-webui-forge)](https://github.com/lllyasviel/stable-diffusion-webui-forge) | required | 8G | Forge, a more VRAM-efficient WebUI fork | AGPL-3.0 |
| [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts) | [![Stars](https://img.shields.io/github/stars/kohya-ss/sd-scripts)](https://github.com/kohya-ss/sd-scripts) | required | 8G | LoRA / fine-tune scripts; common for character style | Apache-2.0 |

## Related lists

| Project | ★ | NVIDIA | VRAM | One-liner |
|---|---|---|---|---|
| [mantoufan/awesome-text-to-video](https://github.com/mantoufan/awesome-text-to-video) | [![Stars](https://img.shields.io/github/stars/mantoufan/awesome-text-to-video)](https://github.com/mantoufan/awesome-text-to-video) | — | — | Text-to-video models vs commercial products; updated often |

## Inclusion rules

1. **Runnable**: has a repo with inference or training code; paper-only homepages stay out of the main tables.
2. **Licensable**: write the license down. Mark `AGPL-3.0`, unspecified, or extra commercial terms in the License column.
3. **Connectable**: prefer projects that plug into motion comics, explainer video, voiceover, or character-consistency pipelines.
4. **Few and current**: keep 1–3 better options per niche; demote or drop older ones.

See [CONTRIBUTING.md](CONTRIBUTING.md) ([English](CONTRIBUTING.en.md)) for how to add an entry. Keep the Chinese and English READMEs in sync.
