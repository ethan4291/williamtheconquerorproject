from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, template_folder='templates')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_PATH = os.path.join(BASE_DIR, 'saved_doc.html')


@app.route('/')
def index():
    PAGE_TITLE = "William the Conqueror Project"

    BOX_TOP = "What I see: French and English soldiers fighting in the Battle of Hastings."
    BOX_RIGHT = "What I hear: Swords clashing and cries of battle coming from across the field."
    BOX_BOTTOM = "What I smell: The forests of England."
    BOX_LEFT = "What I sense: The armies smashing together as they charge into battle."
    BOX_EXTRA = "What actions I might take: Leading the armies to take over England."

    IMAGE_SRC = "static/williamtheconqueror.jpg"

    ESSAY_BODY = (
        f"""
        <div class="figure" role="group" aria-label="Sensory figure">
            <div class="box box-extra">{BOX_EXTRA}</div>
            <div class="box box-top">{BOX_TOP}</div>
            <div class="box box-left">{BOX_LEFT}</div>
            <div class="box box-center">{f'<img src="{IMAGE_SRC}" alt="center image">' if IMAGE_SRC else ''}</div>
            <div class="box box-right">{BOX_RIGHT}</div>
            <div class="box box-bottom">{BOX_BOTTOM}</div>
        </div>
        """
    )

    html = f"""
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>{PAGE_TITLE}</title>
            <style>
                body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }}
                .container {{ min-height: 100vh; display: flex; align-items: flex-start; justify-content: center; padding-top: 6vh; }}
                .content {{ max-width: 760px; padding: 24px; }}
                h1 {{ margin: 0 0 16px 0; font-size: 28px; text-align: center; }}
                .essay {{ white-space: pre-wrap; line-height: 1.6; color: #111; }}
                .essay .indent {{ text-indent: 2em; margin-top: 12px; }}
                /* Sensory figure layout */
                .figure {{ display: grid; grid-template-columns: 1fr 260px 1fr; grid-template-rows: 100px 260px 100px; gap: 12px; align-items: center; justify-items: center; }}
                .box {{ border: 1px solid #d0d0d0; background: #fafafa; padding: 10px; box-sizing: border-box; width: 100%; max-width: 260px; text-align: center; border-radius: 6px; }}
                .box-top {{ grid-column: 2; grid-row: 1; }}
                .box-left {{ grid-column: 1; grid-row: 2; }}
                .box-center {{ grid-column: 2; grid-row: 2; display:flex; align-items:center; justify-content:center; padding: 6px; background: transparent; border: none; max-width: none; }}
                .box-center img {{ max-width: 220px; max-height: 220px; object-fit: cover; border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }}
                .box-right {{ grid-column: 3; grid-row: 2; }}
                .box-bottom {{ grid-column: 2; grid-row: 3; }}
                .box-extra {{ grid-column: 1; grid-row: 1; max-width: 200px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="content">
                    <h1>{PAGE_TITLE}</h1>
                    <div class="essay">{ESSAY_BODY}</div>
                </div>
            </div>
        </body>
    </html>
    """
    return html


@app.route('/save', methods=['POST'])
def save():
    html = request.json.get('html', '')
    try:
        with open(SAVE_PATH, 'w', encoding='utf-8') as f:
            f.write(html)
        return jsonify({'status': 'ok'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/saved')
def saved():
    if os.path.exists(SAVE_PATH):
        return send_from_directory(BASE_DIR, 'saved_doc.html')
    return 'No saved document yet', 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
