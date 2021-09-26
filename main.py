import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders

triangle = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0,  0.5, 0.0]


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



VBO = glGenBuffers(1)       # create buffer for vertex and generate id
glBindBuffer(GL_ARRAY_BUFFER, VBO)  #create type of buffer
glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW) #copy data in buffer memory

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

    # Make the window's context current
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Input esc
        processInput(window)

        # Render here, e.g. using pyOpenGL
        glClearColor(0.7, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)



        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
