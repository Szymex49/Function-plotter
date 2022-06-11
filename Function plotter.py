from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib import rc
from tokenize import TokenError
import tkinter as tk
import sympy as sp
import numpy as np


def function_drawer():
    """Display a graphic interface containing:
    - place to enter a function formulas
    - keyboard with symbols, arithmetic operators and elementary functions
    - plot image
    - possibility to change the settings of the plot
    Convert the entered formulas to functions and draw their plots in the given x-range.
    If the formula or x limits are incorrect, display an error message."""

    x = sp.symbols('x')
    color = '#D2EBFF'


    # Main options
    root = tk.Tk()
    root.title('Function Plotter')
    root.config(bg=color)
    root.iconbitmap('function_drawer.ico')
    root.resizable(False, False)


    # ======== VARIOUS WIDGETS ========


    # An empty space at the top
    empty_top = tk.Label(root, bg=color)
    empty_top.grid(row=0, column=1)

    # An empty space between the keyboard and the plot
    empty_between = tk.Label(root, width=3, bg=color)
    empty_between.grid(row=3, column=5, rowspan=7)

    # An empty space on the right side
    empty_between = tk.Label(root, bg=color)
    empty_between.grid(row=1, column=12)

    # An empty space where warnings will be shown
    warning_place = tk.Label(root, height=3, bg=color)
    warning_place.grid(row=2, column=1, columnspan=7)

    # An empty space where plots will be shown
    empty_fig = plt.figure(figsize=(5, 5))
    empty_fig.set_facecolor(color)
    empty_space = FigureCanvasTkAgg(empty_fig, root)
    empty_space.get_tk_widget().grid(row=3, column=6, rowspan=7, columnspan=2)

    # f(x) =
    f_x = tk.Label(root, text='f(x) =', font='Calibri 20', bg=color)
    f_x.grid(row=1, column=1, sticky='NESW')


    # A place to enter a function formulas
    entry = tk.Entry(root)
    entry.config(font='Calibri 20', bd=3, width=45)
    entry.grid(row=1, column=2, columnspan=5, sticky='NESW')


    # End button
    end_button = tk.Button(root, text='QUIT', command=exit, font='Calibri 20 bold', bg='#cc0000')
    end_button.grid(row=9, column=9, columnspan=4, sticky='NESW')


    # ======== PLOT SETTINGS ========


    # X-axis name
    x_name_text = tk.Label(root, text='X-axis name:', font='Calibri 15', bg=color)
    x_name_text.grid(row=1, column=8, sticky='E')

    # A place to enter X-axis name
    x_name = tk.Entry(root)
    x_name.config(font='Calibri 15')
    x_name.grid(row=1, column=9, columnspan=3, sticky='EW')


    # Y-axis name
    y_name_text = tk.Label(root, text='Y-axis name:', font='Calibri 15', bg=color)
    y_name_text.grid(row=2, column=8, sticky='E')

    # A place to enter Y-axis name
    y_name = tk.Entry(root)
    y_name.config(font='Calibri 15')
    y_name.grid(row=2, column=9, columnspan=3, sticky='EW')


    # Plot title
    plot_title_text = tk.Label(root, text='Plot title:', font='Calibri 15', bg=color)
    plot_title_text.grid(row=3, column=8, sticky='E')

    # A place to enter a plot title
    plot_title = tk.Entry(root)
    plot_title.config(font='Calibri 15')
    plot_title.grid(row=3, column=9, columnspan=3, sticky='EW')


    # X-axis range
    x_range_text = tk.Label(root, text='X-axis range', font="Calibri 20", bg=color)
    x_range_text.grid(row=4, column=9, columnspan=3, sticky='S')

    # A place to enter x lower limit
    x_low_lim = tk.Entry(root)
    x_low_lim.config(width=8, justify='center', font="Calibri 20")
    x_low_lim.grid(row=5, column=9, sticky='NE')

    # A space between entries
    x_between = tk.Label(root, text=':', font="Calibri 20", bg=color)
    x_between.grid(row=5, column=10, sticky='N')

    # A place to enter x upper limit
    x_up_lim = tk.Entry(root)
    x_up_lim.config(width=8, justify='center', font="Calibri 20")
    x_up_lim.grid(row=5, column=11, sticky='NW')


    # Y-axis range
    y_range_text = tk.Label(root, text='Y-axis range', font="Calibri 20", bg=color)
    y_range_text.grid(row=6, column=9, columnspan=3, sticky='S')

    # A place to enter y lower limit
    y_low_lim = tk.Entry(root)
    y_low_lim.config(width=8, justify='center', font="Calibri 20")
    y_low_lim.grid(row=7, column=9, sticky='NE')

    # A space between entries
    y_between = tk.Label(root, text=':', font="Calibri 20", bg=color)
    y_between.grid(row=7, column=10, sticky='N')

    # A place to enter y upper limit
    y_up_lim = tk.Entry(root)
    y_up_lim.config(width=8, justify='center', font="Calibri 20")
    y_up_lim.grid(row=7, column=11, sticky='NW')


    # Checkbox for legend choice
    legend_value = tk.BooleanVar()
    legend_choice = tk.Checkbutton(root, variable=legend_value, onvalue=True, offvalue=False, text='Show legend', bg=color, font='Calibri 15')
    legend_choice.grid(row=8, column=9, columnspan=3, sticky='N')


    # ======== KEYBOARD ========


    def add_text(text):
        entry.insert(tk.INSERT, text)

    def set_cursor(index):
        entry.icursor(entry.index(tk.INSERT) + index)

    def remove_one():
        entry.delete(entry.index(tk.INSERT)-1, entry.index(tk.INSERT))


    # Clear
    plus_but = tk.Button(root, text='Clear', font='Calibri 20', command=lambda: entry.delete(0, tk.END))
    plus_but.grid(row=3, column=1, columnspan=2, sticky='NESW')

    # Backspace ⤺
    plus_but = tk.Button(root, text='⤺', font='Calibri 25', command=remove_one)
    plus_but.grid(row=3, column=3, columnspan=2, sticky='NESW')

    # +
    plus_but = tk.Button(root, text='+', font='Calibri 25', padx=20, command=lambda: add_text('+'))
    plus_but.grid(row=4, column=1, sticky='NESW')

    # -
    minus_but = tk.Button(root, text='−', font='Calibri 25', padx=30, command=lambda: add_text('-'))
    minus_but.grid(row=4, column=2, sticky='NESW')

    # ×
    plus_but = tk.Button(root, text='×', font='Calibri 25', padx=30, command=lambda: add_text('*'))
    plus_but.grid(row=4, column=3, sticky='NESW')

    # /
    plus_but = tk.Button(root, text='/', font='Calibri 25', padx=30, command=lambda: add_text('/'))
    plus_but.grid(row=4, column=4, sticky='NESW')

    # (
    plus_but = tk.Button(root, text='(', font='Calibri 25', command=lambda: add_text('('))
    plus_but.grid(row=5, column=1, sticky='NESW')

    # (
    plus_but = tk.Button(root, text=')', font='Calibri 25', command=lambda: add_text(')'))
    plus_but.grid(row=5, column=2, sticky='NESW')

    # e
    plus_but = tk.Button(root, text='e', font='Calibri 25', command=lambda: add_text('E'))
    plus_but.grid(row=5, column=3, sticky='NESW')

    # π
    plus_but = tk.Button(root, text='π', font='Calibri 25', command=lambda: add_text('pi'))
    plus_but.grid(row=5, column=4, sticky='NESW')

    # a²
    plus_but = tk.Button(root, text='a²', font='Calibri 25', command=lambda: add_text('**2'))
    plus_but.grid(row=6, column=1, sticky='NESW')

    # aᶜ
    plus_but = tk.Button(root, text='aᶜ', font='Calibri 25', command=lambda: add_text('**'))
    plus_but.grid(row=6, column=2, sticky='NESW')

    # √
    plus_but = tk.Button(root, text='√', font='Calibri 25', command=lambda: add_text('sqrt()') or set_cursor(-1))
    plus_but.grid(row=6, column=3, sticky='NESW')

    # ∛
    plus_but = tk.Button(root, text='∛', font='Calibri 25', command=lambda: add_text('root(, 3)') or set_cursor(-4))
    plus_but.grid(row=6, column=4, sticky='NESW')

    # x
    plus_but = tk.Button(root, text='x', font='Calibri 25', command=lambda: add_text('x'))
    plus_but.grid(row=7, column=1, sticky='NESW')

    # |a|
    plus_but = tk.Button(root, text='|a|', font='Calibri 25', command=lambda: add_text('Abs()') or set_cursor(-1))
    plus_but.grid(row=7, column=2, sticky='NESW')

    # logₐ(b)
    plus_but = tk.Button(root, text='logₐb', font='Calibri 20', command=lambda: add_text('log(b, a)') or set_cursor(-4))
    plus_but.grid(row=7, column=3, sticky='NESW')

    # ln
    plus_but = tk.Button(root, text='ln', font='Calibri 20', command=lambda: add_text('ln()') or set_cursor(-1))
    plus_but.grid(row=7, column=4, sticky='NESW')

    # sin
    plus_but = tk.Button(root, text='sin', font='Calibri 20', command=lambda: add_text('sin()') or set_cursor(-1))
    plus_but.grid(row=8, column=1, sticky='NESW')

    # cos
    plus_but = tk.Button(root, text='cos', font='Calibri 20', command=lambda: add_text('cos()') or set_cursor(-1))
    plus_but.grid(row=8, column=2, sticky='NESW')

    # tan
    plus_but = tk.Button(root, text='tan', font='Calibri 20', command=lambda: add_text('tan()') or set_cursor(-1))
    plus_but.grid(row=8, column=3, sticky='NESW')

    # cot
    plus_but = tk.Button(root, text='cot', font='Calibri 20', command=lambda: add_text('(1/tan())') or set_cursor(-2))
    plus_but.grid(row=8, column=4, sticky='NESW')

    # asin
    plus_but = tk.Button(root, text='asin', font='Calibri 20', command=lambda: add_text('asin()') or set_cursor(-1))
    plus_but.grid(row=9, column=1, sticky='NESW')

    # acos
    plus_but = tk.Button(root, text='acos', font='Calibri 20', command=lambda: add_text('acos()') or set_cursor(-1))
    plus_but.grid(row=9, column=2, sticky='NESW')

    # atan
    plus_but = tk.Button(root, text='atan', font='Calibri 20', command=lambda: add_text('atan()') or set_cursor(-1))
    plus_but.grid(row=9, column=3, sticky='NESW')

    # acot
    plus_but = tk.Button(root, text='acot', font='Calibri 20', command=lambda: add_text('atan(1/)') or set_cursor(-1))
    plus_but.grid(row=9, column=4, sticky='NESW')


    # ======== DRAWING PLOT ========


    plot_widget = tk.Label(root)
    fig = plt.figure()


    def display_error(text):
        """Display a widget with an error message."""
        error = tk.Label(root, text=text, font='Calibri 15', fg='red', bg=color)
        error.grid(row=2, column=1, columnspan=4)
        error.after(1500, error.destroy)
        plot_widget.destroy()
        plt.close(fig)


    def draw_plot():
        """Calculate values of the functions in the given x-range.
        Display a widget with plots of the functions."""

        nonlocal fig
        nonlocal plot_widget
        plt.close(fig)
        plot_widget.destroy()  # Remove the last plot

        # If function hasn't been entered, display an error
        if entry.get() == '':
            display_error('Enter a function formula.')
            return

        fig = plt.figure(figsize=(5, 5))
        fig.set_facecolor(color)
        ax = fig.add_subplot(111)

        # If x limits hasn't been entered
        if x_low_lim.get() == '' or x_up_lim.get() == '':
            display_error('Enter X-axis limits.')
            return

        # x values
        try:
            xs = np.linspace(float(x_low_lim.get()), float(x_up_lim.get()), 1000)
        except ValueError:
            display_error('Incorrect X-axis limits.')
            return

        functions = entry.get().split(';')
        counter = 0

        # For each function find a formula and draw a plot
        for function in functions:
            counter += 1  # Number of function

            # Remove the space before the formula
            if function[0] == ' ':
                function = function[1:]

            # Find the function formula
            try:
                expression = sp.parse_expr(function)
                formula = sp.lambdify(x, expression, 'numpy')
            except (SyntaxError, TypeError, KeyError, TokenError):
                display_error('Incorrect function ' + str(counter) + ' formula.')
                return

            # Calculate y values
            try:
                ys = formula(xs)
                if type(ys) == int or type(ys) == float:  # If the function is constant
                    ys = np.linspace(formula(0), formula(0), 1000)
            except NameError:
                display_error('Incorrect function ' + str(counter) + ' formula.')
                return

            # Find the asymptotes of the function
            try:
                asymptotes = sp.solve(1/expression, x)
                for asymptote in asymptotes:
                    for arg_x, index in zip(xs, range(len(xs))):
                        if arg_x > asymptote:
                            ys[index] = np.nan
                            break
            except (TypeError, NotImplementedError):
                pass

            # Draw plot
            try:
                ax.plot(xs, ys, label='$' + sp.latex(expression) + '$')
            except ValueError:
                display_error('Incorrect function ' + str(counter) + ' formula.')
                return

            # Add horizontal line in y = 0
            if min(ys) < 0 < max(ys):
                plt.axhline(0, linewidth=0.5, linestyle='--', color='#5C5E63')

        # Get y upper limit
        try:
            y_max = float(y_up_lim.get())
        except ValueError:
            y_max = None

        # Get y lower limit
        try:
            y_min = float(y_low_lim.get())
        except ValueError:
            y_min = None

        # Plot options
        plt.ylim(ymin=y_min, ymax=y_max)
        ax.set_title(plot_title.get())
        ax.set_xlabel(x_name.get())
        ax.set_ylabel(y_name.get())
        if legend_value.get():
            rc('text', usetex=True)
            ax.legend(loc=1, fontsize=16)
            rc('text', usetex=False)

        # Add vertical line in x = 0
        if float(x_low_lim.get()) < 0 and float(x_up_lim.get()) > 0:
            plt.axvline(0, linewidth=0.5, linestyle='--', color='#5C5E63')

        # Create a widget with plot
        plots = FigureCanvasTkAgg(fig, root)
        plot_widget = plots.get_tk_widget()
        plot_widget.grid(row=3, column=6, rowspan=7, columnspan=2)


    # The main button which draws plots
    main_button = tk.Button(root, text='DRAW', font='Calibri 20', width=10, bg='#1FAD29', command=draw_plot)
    main_button.grid(row=1, column=7, sticky='W')

    root.mainloop()


function_drawer()
