from cg import CGDefaultShader
import os

class BlurShader(CGDefaultShader):
    VERTICAL, HORIZONTAL = list(range(2))

    def __init__(self, size=(800,800), radius=10, sigma=3):
        self.width, self.height = size
        
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        with open('%s/blur.cg' % cur_dir) as f:
            from mako.template import Template
            source = bytes(str(Template(f.read()).render(
                sigma=sigma,
                radius=radius,
                )), 'ascii')
        # print('trying to compile blur.cg. source: ')
        # source = open('%s/blur2.cg' % cur_dir).read().strip()
        # print(source)
        super(BlurShader, self).__init__(source, entry_vertex=b"passVertex", entry_fragment=b"blurFragment")
        
        self.direction = BlurShader.HORIZONTAL
        self.sigma = sigma

        self._direction = self.get_parameter("direction")
        # self.radius = radius
        # self._radius = self.get_parameter("radius")
        # self._sigma = self.get_parameter("sigma")
        self._texelSize = self.get_parameter("texelSize")

    from contextlib import contextmanager
    @contextmanager
    def blur(self, direction):
        self.direction = direction
        with self:
            yield

    def set_default_parameters(self):
        #self._radius.setf(self.radius)
        #self._sigma.setf(self.sigma)
        if self.direction == BlurShader.HORIZONTAL:
            self._direction.set2f(1,0)
            self._texelSize.setf(1./self.width)
        else:
            self._direction.set2f(0,1)
            self._texelSize.setf(1./self.height)
