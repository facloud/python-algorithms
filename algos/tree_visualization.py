from __future__ import print_function


def draw_node(node, prefix='', last=False):
    print('<{}>'.format(node.value))
    if last:
        prefix = prefix + '  '
    else:
        prefix = prefix + '| '
    for i in range(0, len(node.children)):
        print('{}|_'.format(prefix), end='')
        draw_node(
            node.children[i],
            prefix,
            i == len(node.children) - 1
        )

def draw_tree(tree):
    draw_node(tree, '', True)
