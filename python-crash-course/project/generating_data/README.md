## Generating Data
Data visualization involves exploring data
through visual representations. It’s closely
associated with data analysis, which uses code
to explore the patterns and connections in a data
set. A data set can be made up of a small list of numbers
that fits in one line of code or it can be many gigabytes
of data.

Making beautiful data representations is about more than pretty pictures.
When a representation of a data set is simple and visually appealing,
its meaning becomes clear to viewers. People will see patterns and significance
in your data sets that they never knew existed.
Fortunately, you don’t need a supercomputer to visualize complex data.
With Python’s efficiency, you can quickly explore data sets made of millions
of individual data points on just a laptop. Also, the data points don’t have to
be numbers. With the basics you learned in the first part of this book, you
can analyze nonnumerical data as well.

#### Installing Matplotlib

To use Matplotlib for your initial set of visualizations, you’ll need to install
it using pip, a module that downloads and installs Python packages. Enter
the following command at a terminal prompt:

#### Plotting a Simple Line Graph
Let's plot a simple line graph using Matplotlib, and then customize it to create a more informative data visualization.
We first import the pyplot module using the alias plt so we don’t have to
type pyplot repeatedly. (You’ll see this convention often in online examples,
so we’ll do the same here.) The pyplot module contains a number of functions
that generate charts and plots.
We create a list called squares to hold the data that we’ll plot. Then we
follow another common Matplotlib convention by calling the subplots()
function . This function can generate one or more plots in the same figure.
The variable fig represents the entire figure or collection of plots that
are generated. The variable ax represents a single plot in the figure and is
the variable we’ll use most of the time.

#### Chaning the Label Type and Line Thickness
The linewidth parameter at  controls the thickness of the line that
plot() generates. The set_title() method at  sets a title for the chart. The
fontsize parameters, which appear repeatedly throughout the code, control
the size of the text in various elements on the chart.
The set_xlabel() and set_ylabel() methods allow you to set a title for
each of the axes , and the method tick_params() styles the tick marks .
The arguments shown here affect the tick marks on both the x- and y-axes
(axis='both') and set the font size of the tick mark labels to 14 (labelsize=14).