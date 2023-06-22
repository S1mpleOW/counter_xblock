"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope


class CounterXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the CounterXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/counter.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/counter.css"))
        frag.add_javascript(self.resource_string("static/js/src/counter.js"))
        frag.initialize_js('CounterXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def update_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        self.count += data['count'] if data['count'] is not None else 0
        return {"count": self.count}

    @XBlock.json_handler
    def reset_count(self, data, suffix=''):
        """
        An example handler, which resets the data.
        """
        self.count = 0
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("CounterXBlock",
             """<counter/>
             """),
            ("Multiple CounterXBlock",
             """<vertical_demo>
                <counter/>
                <counter/>
                <counter/>
                </vertical_demo>
             """),
        ]
