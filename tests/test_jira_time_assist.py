from .context import jira_time_assist

def test_jira_time_assist(capsys, example_fixture):
    jira_time_assist.JiraTimeAssistant.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out