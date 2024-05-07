## Examining the Performance and Reasoning of Competing LLMs in Language-Based, Competitive Environments
### Kevin Li, Connor Rabinowitz, Zhuoxuan Zhang, Louis Zheng

This repository and codebase was forked from https://github.com/jinhaoduan/GTBench, the original repository by the authors of [GTBENCH: Uncovering the Strategic Reasoning Limitations of
LLMs via Game-Theoretic Evaluations](https://arxiv.org/pdf/2402.12348). We modified and added new files - to extend the framework to the analysis of two new games not covered in the original suite of games provided by the authors. 

The new files include: 
1. NRA_test.py - testing framework that allows us to compare NRA values and Completion Rates of ModelxReasoning Type with GPT-3.5 TurboxPrompt.
2. /gamingbench/games/crazy_eights.py and /gamingbench/games/dots_and_boxes.py - code that allows translation from OpenSpiel framework implementation to LLM token response and vice versa.
3. /gamingbench/prompts/observation_prompts/crazy_eights.py and /gamingbench/prompts/observation_prompts/crazy_eights.py - code that produces the head prompt and observation prompt that is directed towards the LLM.

There have been other minor additions in terms of config files. 

To run the NRA_test.py to produce results, please follow this set of steps: 
1. Clone this [repository](https://github.com/ZhuoxuanZhangHarry/GTBench). 
2. Access your [OpenAI API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) and [DeepInfra](https://deepinfra.com/) API Key.
3. Update NRA_test.py and /gamingbench/chat/chat.py with copied API Keys. Ctrl-F for "api" to see where to enter these.
4. Run NRA_test.py with the following command line arguments:

   python3 NRA_test.py {game} {opponent_llm_model} {llm_reasoning_type} {num_matches}

      example: python3 NRA_test.py crazy_eights gpt-4-turbo prompt_agent 50

6. Access the produced information under the newly created /experiments_{TIME_AT_RUN} folder. Each match will have its own subdirectory contained the json log file with overall game information and .log files with historical record of the gameplay and LLM interaction and response. After all matches have ended, a run_log.txt (which is updated throughout the run) will finish producing with information on number of matches, winning players, player scores at end, final NRA value, and completion rates.

Note our codebase supports GPT-4-Turbo, GPT-3.5-Turbo, CodeLlama-34b-Instruct and Llama-2-7b-chat. Prompt, Chain of Thought (CoT), and Self-contained Chain Thought (ScCoT) have been tested and confirmed to be supported with our implementation. 

