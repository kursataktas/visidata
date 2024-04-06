'ASCII monochrome theme; default colors only'

from visidata import vd


vd.themes['asciimono'] = dict(
    disp_note_none='',
    disp_truncator='>',
    disp_oddspace='.',
    disp_more_left='<',
    disp_more_right='>',
    disp_error_val='',
    disp_ambig_width=1,

    disp_pending='',
    note_pending=':',
    note_format_exc='?',
    note_getter_exc='!',
    note_type_exc='!',

    color_note_pending='bold',
    color_note_type='',
    color_note_row='',

    disp_column_sep='|',
    disp_keycol_sep='|',
    disp_rowtop_sep='|',
    disp_rowmid_sep='|',
    disp_rowbot_sep='|',
    disp_rowend_sep='|',
    disp_keytop_sep='|',
    disp_keymid_sep='|',
    disp_keybot_sep='|',
    disp_endtop_sep='|',
    disp_endmid_sep='|',
    disp_endbot_sep='|',
    disp_selected_note='+',
    disp_sort_asc='^^^^^^',
    disp_sort_desc='vvvvvv',
    color_default='',
    color_default_hdr='bold',
    color_bottom_hdr='underline',
    color_current_row='reverse',
    color_current_col='bold',
    color_current_hdr='bold reverse',
    color_column_sep='',
    color_key_col='bold',
    color_hidden_col='8',
    color_selected_row='',
    color_edit_cell='',
    color_edit_unfocused='',
    color_graph_hidden='',
    color_graph_selected='bold',
    color_status_replay='',
    color_currency_neg='',
    color_match='',
    color_cmdpalette='',

    color_graph_axis='bold',
    color_sidebar='reverse',
    color_change_pending='reverse',
    color_delete_pending='underline',

    disp_rstatus_fmt=' {sheet.longname} {sheet.nRows:9d} {sheet.rowtype} {sheet.modifiedStatus} {sheet.options.disp_selected_note}{sheet.nSelectedRows}',
    disp_status_fmt='{sheet.shortcut}> {sheet.name}| ',
    disp_lstatus_max=0,
    disp_status_sep=' | ',
    color_keystrokes='bold reverse',
    color_status='bold reverse',
    color_error='bold',
    color_warning='bold',
    color_top_status='underline',
    color_active_status='reverse',
    color_inactive_status='8',
    color_working='',
    color_longname='',
    color_highlight_status='',
    color_sidebar_title='',
    color_heading='',
    color_guide_unwritten='',
    color_code='',

    color_menu='reverse',
    color_menu_active='',
    color_menu_spec='reverse',
    color_menu_help='reverse',
    color_add_pending='',
    disp_menu_boxchars='||--    ||',
    disp_menu_more='>',
    disp_menu_push='+',
    disp_menu_input='_',
    disp_menu_fmt='_.;"`\\ ASCII mono /\':._',
    plot_colors = 'white',
)
