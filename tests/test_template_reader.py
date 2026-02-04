from src import template_reader


def test_read_template():
    template = template_reader.read_template('templates/test_template.json')
    assert 'box_list' in template
    assert len(template['box_list']) == 6
    assert template['box_list'][0]['title'] == 'VN JAT'
    assert template['box_list'][1]['title'] == '15 Min. Pause'
    assert template['box_list'][2]['start'] == '11:00'
    assert template['box_list'][-1]['title'] == 'Arbeitstag abschließen'
    assert template['box_list'][-1]['type'] == 'default'
    assert template['box_list'][3]['zone'] == 'Europe/Berlin'
