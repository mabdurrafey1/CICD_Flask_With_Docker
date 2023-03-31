from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/')
def index():
    return jsonify({"hello":"world"})

@application.route('/check_overlap', methods=['POST'])
def check_overlap():
    try:
        data = request.get_json()
        
        if not data:
            raise ValueError("No data provided")

        range1_start = data['range1']['start']
        range1_end = data['range1']['end']
        range2_start = data['range2']['start']
        range2_end = data['range2']['end']

        status= range1_start < range2_end and range1_end > range2_start
        
        response = {
            'overlap': status
        }
        
        return jsonify(response)
    
    except KeyError as e:
        return jsonify({'error': f'Missing key: {e.args[0]}' }), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    application.run(debug=True)
