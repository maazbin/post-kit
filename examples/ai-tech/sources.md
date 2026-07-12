# Sources

## Core Rule

Trending = 2+ independent channels + velocity (engagement/hour). One source alone = skip.

## Source Layers

**L1 Real-Time:**
- HackerNews front page
- r/MachineLearning (hot + rising)
- r/LocalLLaMA (hot + rising)
- Google Trends
- Techmeme

**L2 Research:**
- HuggingFace Papers
- arXiv (cs.AI, cs.LG, cs.CL)
- Papers with Code

**L3 Builders:**
- GitHub Trending (Python, daily)
- HuggingFace Models (new releases)
- Product Hunt

**L4 Context:**
- TechCrunch
- MIT Tech Review
- Ars Technica

## Global Coverage

| Region | Track Via |
|--------|-----------|
| China (DeepSeek, Qwen, Baidu) | r/LocalLLaMA, HuggingFace downloads |
| Europe (Mistral, DeepMind London) | Techmeme, arXiv affiliations |
| Open Source global (Ollama, vLLM, llama.cpp) | GitHub velocity, r/LocalLLaMA |

## Scouting Routine (MCP-Powered)

```
AM:
1. hackernews get_stories(top, 30) → filter AI/ML keywords
2. reddit hot posts r/MachineLearning (limit 15)
3. reddit rising posts r/LocalLLaMA (limit 10)
4. github-trending daily (language: python)

Cross-validate:
5. Topic in 2+ of above? → post candidate
6. Web search → scrape source for full context
7. hackernews search("[topic]") → check community sentiment

PM (optional):
8. github-trending weekly → slower signals
9. reddit top posts r/MachineLearning (time: day)
```

## Urgency

- Emerging (0.7-1.0): Post immediately
- Peak (0.4-0.7): Only with unique angle
- Stable (0.15-0.4): Queue for slow days
- Declining (<0.15): Skip

## Anti-Bias Gate

Before posting, check:
1. Appears in 2+ independent sources from different layers?
2. Would this get equal coverage if a non-US company did it?
3. Is this impact (benchmarks, users, code) or just announcement?
4. Who did similar work and got zero coverage?
