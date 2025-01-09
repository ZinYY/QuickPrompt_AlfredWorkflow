# QuickPrompt - Alfred Workflow

[中文说明](readme.md)

QuickPrompt is an Alfred workflow designed to enhance text input efficiency by providing quick access to predefined prompts.

When working with large language models, users often need to input specific prompts to enhance the quality of model outputs. This workflow enables quick access to various preset scenarios through the hotkey `Command + .`, allowing you to efficiently input these prompts.

![Example](figs/example.png)

## Features

- Global hotkey `Command + .` for instant access
- Multiple preset scenarios:

    - 🔠⇨🔠 Academic English Writing Polish
    - 📚 Bibtex Citation Format
    - 🔠⇨🀄️ English to Chinese Translation (Academic)
    - ... ...

- Automatically cache the last search results

- After installation the workflow, you can customize prompts by modifying the `Workflows -> QuickPrompt -> Script Filter` in Alfred.

## Installation

Download `QuickPrompt.alfredworkflow` from the [Release page](https://github.com/ZinYY/QuickPrompt_AlfredWorkflow/releases) and double-click to install.

Open `Workflows -> QuickPrompt -> Hotkey`, set the hotkey (recommended `Command + .`)

![Set Hotkey](figs/set_hotkey.png)

## How to Use

1. Press `Command + .` to invoke QuickPrompt
2. Type keywords to search for desired prompts (supports both English and Chinese)
3. Select the prompt, and it will be automatically inserted at the beginning of the text

## Search Tips

- Supports both English and Pinyin search:
    - "polish" - for writing polish prompts
    - "bibtex" - for citation format prompts
    - "translate" or "fanyi" - for translation prompts
    - "code" - for code explanation prompts

## Author

Created by Yu-Yang Qian

## Sponsor

If you find this Alfred workflow useful, please consider supporting the author with a coffee:

![sponsor](figs/pic_receive.jpg)
