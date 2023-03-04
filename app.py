from flask import Flask, render_template, request, redirect, session, abort
import openai

def format_text(text):
    lines = []
    current_line = ''
    for char in text:
        if char.isdigit() and (char == '1' or current_line[-1:].isspace()):
            if current_line.endswith('.') or current_line.endswith(')'):
                current_line += '\n'
        current_line += char
        if char == '\n':
            lines.append(current_line.rstrip())
            current_line = ''
    lines.append(current_line.rstrip())
    return '\n'.join(lines)

# Initialize Flask app
app = Flask(__name__)

# 配置 Jinja2 模板引擎
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Initialize OpenAI API key
openai.api_key = 'YOUR-OPENAI-API-KEY'

# Define chat route
messages = [{"role": "system", "content": "You are an assistant."}]
tokens = 1
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global messages
    global tokens
    if request.method == 'POST':
        message = request.form['message']
        messages.append({"role": "user", "content": message})
        try:
            response = openai.ChatCompletion.create (
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.8
            )
        except openai.error.InvalidRequestError:
            reply="哎呀，超出最长的上下文记忆了，请开始一段新的对话"
            messages = [{"role": "system", "content": "哎呀，超出最长的上下文记忆了，请开始一段新的对话"}]
        else:       
            reply = format_text(response.choices[0].message.content)
            tokens = response.usage.total_tokens
            messages.append({"role": "assistant", "content": reply}) 
            print(reply)
        return render_template('chat.html', messages=messages, message=message)
    return render_template('chat.html', messages=messages)

@app.route('/logout')
def logout():
    global messages
    messages = [{"role": "system", "content": "You are an assistant."}]
    return redirect('/chat')

# Run app
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
