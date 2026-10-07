import runpy
from pathlib import Path
from unittest.mock import MagicMock, patch

def load():
    tk, openai = MagicMock(), MagicMock()
    with patch.dict('sys.modules', {'tkinter':tk, 'openai':openai}):
        module = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'main.py'))
    return module, tk, openai

def test_submit_sends_prompt_and_displays_completion():
    module, tk, openai = load()
    module['text_box'].get.return_value = 'Explain recursion'
    openai.Completion.create.return_value = {'choices':[{'text':'A function calling itself.'}]}
    module['display_text']()
    assert openai.Completion.create.call_args.kwargs['prompt'] == 'Explain recursion'
    assert openai.Completion.create.call_args.kwargs['max_tokens'] == 500
    module['output_label'].config.assert_called_with(text='A function calling itself.')

def test_select_all_uses_full_text_range():
    module, tk, _ = load()
    module['select_text'](None)
    module['text_box'].tag_add.assert_called_once_with(tk.SEL, '1.0', tk.END)
