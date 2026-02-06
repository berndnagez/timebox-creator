from src import template


def test_read_template():
    loaded_template = template.read_template('templates/test_template.json')
    assert 'box_list' in loaded_template
    assert len(loaded_template['box_list']) == 6
    assert loaded_template['box_list'][0]['title'] == 'VN JAT'
    assert loaded_template['box_list'][1]['title'] == '15 Min. Pause'
    assert loaded_template['box_list'][2]['start'] == '11:00'
    assert loaded_template['box_list'][-1]['title'] == 'Arbeitstag abschließen'
    assert loaded_template['box_list'][-1]['type'] == 'default'
    assert loaded_template['box_list'][3]['zone'] == 'Europe/Berlin'
