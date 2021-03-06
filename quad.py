import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy

# input behavior
def processInput(window):
    if glfw.get_key(window, glfw.KEY_ESCAPE):
        print("window_should_close")
        glfw.window_should_close(window)
        #glfw.Set_Window_Should_Close(window, True)
        glfw.terminate()


def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(940, 480, "Hello glfw", None, None)

    if not window:
        glfw.terminate()
        return

    # Make the window's context current in a stream
    glfw.make_context_current(window)

    # create quad
    quad = [-0.5, -0.5, 0.0,     1, 0, 0,
             0.5, -0.5, 0.0,     0, 1, 0,
             0.5,  0.5, 0.0,     0, 0, 1,
            -0.5,  0.5, 0,       0, 0, 0]

    quad = numpy.array(quad, dtype=numpy.float32)
    print(quad)

    quad_index = [0, 1, 2,
             2, 3, 0]
    quad_index = numpy.array(quad_index, dtype=numpy.uint32)

# create shaders
    vertex_shader = """
        #version 330
        in vec3 position;
        in vec3 color;
        out vec3 newColor;
        void main()
        {
            gl_Position = vec4(position, 1.0f);
            newColor = color;
        }
        """

    fragment_shader = """
        #version 330
        in vec3 newColor;
        out vec4 outColor;
        void main()
        {
            outColor = vec4(newColor, 1.0f);
        }
        """

    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))


    VBO = glGenBuffers(1)  # create buffer for vertex and generate id
    glBindBuffer(GL_ARRAY_BUFFER, VBO)  # create type of buffer
    glBufferData(GL_ARRAY_BUFFER, 96, quad, GL_STATIC_DRAW)  # copy data in buffer memory

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 24, quad_index, GL_STATIC_DRAW)


    posAttrib = glGetAttribLocation(shader, "position")  # get link between attribute and vertex
    #glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 0, 0)  # ?????? ???????????? ?????????????????????? ???? ??????????????(???????????????? ?????????? ??????????????)
    glVertexAttribPointer(posAttrib, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(posAttrib)  # activation

    color = glGetAttribLocation(shader, "color")  # get link between attribute and vertex
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))  # ?? ?????? ?????????? ???????????????? ????????
    glEnableVertexAttribArray(color)  # activation


    glUseProgram(shader)

    glClearColor(0.1, 0.4, 0.6, 1.0)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Input esc
        processInput(window)

        # Render here, e.g. using pyOpenGL
        glClear(GL_COLOR_BUFFER_BIT)

        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)



        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()