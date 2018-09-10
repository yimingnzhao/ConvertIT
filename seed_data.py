from google.appengine.ext import ndb
from data_objects import Unit, UnitType


def get_seed_data():
    #add basic unit types
    length_key = UnitType(type='length',
        units = ['meter', 'foot', 'inch', 'yard', 'mile', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter']).put()
    meter_key = Unit(name='meter', type='length', abbreviation='m',
        convert_units = ['meter', 'mile', 'foot', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1.0', '0.000621371', '3.28084', '39.37008', '1.09361', '0.00497096', '1e+10', '6.68459e-12', '1.057e-16', '3.24078e-17', '0.001', '1000', '100', '1e+6', '1e+9', '1e-6']).put()
    kilometer_key = Unit(name='kilometer', type='length', abbreviation='km',
        convert_units = ['meter', 'mile', 'foot', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1000', '0.621371', '3280.84', '39370.1', '1093.61', '4.97096', '1e+13', '6.68459e-9', '1.057e-13', '3.24078e-14', '1', '1e+6', '100000', '1e+9', '1e+12', '0.001']).put()
    milimeter_key = Unit(name='milimeter', type='length', abbreviation='mm',
        convert_units = ['meter', 'mile', 'foot', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['0.001', '6.2137e-7', '0.00328084', '0.0393701', '0.00109361', '4.97096e-6', '1e+7', '6.68459e-15', '1.057e-19', '3.24078e-20', '1e-6', '1', '0.1', '1000', '1e+6', '1e-9']).put()
    centimeter_key = Unit(name='centimeter', type='length', abbreviation='cm',
        convert_units = ['meter', 'mile', 'foot', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['0.01', '6.2137e-6', '0.0328084', '0.393701', '0.0109361', '4.97096e-5', '1e+8', '6.68459e-14', '1.057e-18', '3.24078e-19', '1e-5', '10', '1', '10000', '1e+7', '1e-8']).put()
    micrometer_key = Unit(name='micrometer', type='length', abbreviation='&#x3BC;m',
        convert_units = ['meter', 'mile', 'foot', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1e-6', '6.2137e-10', '3.2808e-6', '3.937e-5', '1.0936e-6', '4.97096e-9', '10000', '6.68459e-18', '1.057e-22', '3.24078e-23', '1e-9', '0.001', '1e-10', '1', '0.001', '1e-12']).put()
    megameter_key = Unit(name='megameter', type='length', abbreviation='Mm',
        convert_units = ['meter', 'mile', 'foot', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1000000', '621.371', '3.281e+6', '3.937e+7', '1.094e+6', '4970.96', '1e+16', '6.68459e-6', '1.057e-10', '3.24078e-11', '1000', '1e+9', '1e+8', '1e+12', '1e+15', '1']).put()
    nanometer_key = Unit(name='nanometer', type='length', abbreviation='nm',
        convert_units = ['meter', 'mile', 'foot', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1e-9', '6.2137e-13', '3.2808e-9', '3.937e-8', '1.0936e-9', '4970.96', '1e+16', '6.68459e-6', '1.057e-10', '3.24078e-11', '1000', '1e+9', '1e+8', '1e+12', '1e+15', '1']).put()
    foot_key = Unit(name='foot', type='length', abbreviation='ft',
        convert_units = ['foot', 'mile', 'meter', 'inch', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1.0', '0.000189394', '0.3048', '12.0', '0.333333', '0.00151515', '3.048e+9', '2.03746e-12', '3.22174e-17', '9.8779e-18', '0.0003048', '304.8', '30.48', '304800', '3.048e+8', '3.048e-7']).put()
    inch_key = Unit(name='inch', type='length', abbreviation='in',
        convert_units = ['inch', 'mile', 'meter', 'foot', 'yard', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1.0', '1.5783e-5', '0.0254', '0.0833333', '0.0277778', '0.000126262', '2.54e+8', '1.69789e-13', '2.68478e-18', '8.23158e-19', '2.54e-5', '25.4', '2.54', '25400', '2.54e+7', '2.54e-8']).put()
    yard_key = Unit(name='yard', type='length', abbreviation='yd',
        convert_units = ['yard', 'mile', 'meter', 'inch', 'foot', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1.0', '0.000568182', '0.9144', '36.0', '3.0', '0.00454545', '9.144e+9', '6.11239e-12', '9.66522e-17', '2.96337e-17', '0.0009144', '914.4', '91.44', '914400', '9.144e+8', '9.144e-7']).put()
    mile_key = Unit(name='mile', type='length', abbreviation='mi',
        convert_units = ['yard', 'mile', 'meter', 'inch', 'foot', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1760.0', '1.0', '1609.34', '63360', '5280', '7.99998', '1.609e+13', '1.07578e-8', '1.70108e-13', '5.21553e-14', '1.60934', '1.609e+6', '160934', '1.609e+9', '1.609e+12', '0.00160934']).put()
    furlong_key = Unit(name='furlong', type='length', abbreviation='fur',
        convert_units = ['yard', 'mile', 'meter', 'inch', 'foot', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['220', '0.125', '201.168', '7920.02', '660.001', '1.0', '2.012e+12', '1.34473e-9', '2.12635e-14', '6.51942e-15', '0.201168', '201168', '20116.8', '2.012e+8', '2.012e+11', '0.000201168']).put()
    angstrom_key = Unit(name='angstrom', type='length', abbreviation='&#8491;',
        convert_units = ['yard', 'mile', 'meter', 'inch', 'foot', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1.09361e-10', '6.2137e-14', '1e-10', '3.937e-9', '3.2808e-10', '4.97096e-13', '1.0', '6.68459e-22', '1.057e-26', '3.24078e-27', '1e-13', '1e-7', '1e-8', '1e-4', '0.1', '1e-16']).put()
    astronomical_unit_key = Unit(name='astronomical-unit', type='length', abbreviation='AU',
        convert_units = ['yard', 'mile', 'meter', 'inch', 'foot', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1.636e+11', '9.296e+7', '1.496e+11', '5.89e+12', '4.908e+11', '7.436e+8', '1.496e+21', '1.0', '1.58125e-5', '4.84814e-6', '1.496e+8', '1.496e+14', '1.496e+13', '1.496e+17', '1.496e+20', '149598']).put()
    light_year_key = Unit(name='light-year', type='length', abbreviation='ly',
        convert_units = ['yard', 'mile', 'meter', 'inch', 'foot', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['1.035e+16', '5.879e+12', '9.461e+15', '3.725e+17', '3.104e+16', '4.703e+13', '9.461e+25', '63241.1', '1.0', '0.306601', '9.461e+12', '9.461e+18', '9.461e+17', '9.461e+21', '9.461e+24', '9.461e+9']).put()
    parsec_key = Unit(name='parsec', type='length', abbreviation='pc',
        convert_units = ['yard', 'mile', 'meter', 'inch', 'foot', 'furlong', 'angstrom', 'astronomical-unit', 'light-year', 'parsec', 'kilometer', 'milimeter', 'centimeter', 'micrometer', 'nanometer', 'megameter'],
        convert_values = ['3.375e+16', '1.917e+13', '3.086e+16', '1.215e+18', '1.012e+17', '1.534e+14', '3.086e+26', '206265', '3.26156', '1.0', '3.086e+13', '3.086e+19', '3.086e+18', '3.086e+22', '3.086e+25', '3.086e+10']).put()

    time_key = UnitType(type='time',
        units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond']).put()
    second_key = Unit(name='second', type='time', abbreviation='s',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['1.0', '0.0166667', '0.000277778', '1.1574e-5', '1.6534e-6', '8.2672e-7', '3.8052e-7', '3.171e-8', '1e+9', '1e+6', '1000']).put()
    minute_key = Unit(name='minute', type='time', abbreviation='min',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['60.0', '1.0', '0.0166667', '0.000694444', '9.9206e-5', '4.96032e-5', '2.2831e-5', '1.9026e-6', '6e+10', '6e+7', '60000']).put()
    hour_key = Unit(name='hour', type='time', abbreviation='hr',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['3600.0', '60.0', '1.0', '0.0416667', '0.00595238', '0.00297619', '0.00136986', '0.000114155', '3.6e+12', '3.6e+9', '3.6e+6']).put()
    day_key = Unit(name='day', type='time', abbreviation='d',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['86400.0', '1440.0', '24.0', '1.0', '0.142857', '0.0714286', '0.0328767', '0.00273973', '8.64e+13', '8.64e+10', '8.64e+7']).put()
    week_key = Unit(name='week', type='time', abbreviation='wk',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['604800.0', '10080.0', '168.0', '7.0', '1.0', '0.5', '0.230137', '0.0191781', '6.048e+14', '6.048e+11', '6.048e+8']).put()
    fortnight_key = Unit(name='fortnight', type='time', abbreviation='ftn',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['1.21e+6', '20160.0', '336.0', '14.0', '2.0', '1.0', '0.460273', '0.0383562', '1.21e+15', '1.21e+12', '1.21e+9']).put()
    month_key = Unit(name='month', type='time', abbreviation='m',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['2.628e+6', '43800', '730.001', '30.4167', '4.34524', '2.17262', '1.0', '0.0833334', '2.628e+15', '2.628e+12', '2.628e+9']).put()
    year_key = Unit(name='year', type='time', abbreviation='yr',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['3.154e+7', '525600', '8760', '365', '52.1429', '26.0714', '12', '1.0', '3.154e+16', '3.154e+13', '3.154e+10']).put()
    nanosecond_key = Unit(name='nanosecond', type='time', abbreviation='ns',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['1e-9', '1.6667e-11', '2.7778e-13', '1.1574e-14', '1.6534e-15', '8.2672e-16', '3.8052e-16', '3.171e-17', '1', '0.001', '1e-6']).put()
    microsecond_key = Unit(name='microsecond', type='time', abbreviation='&#x3BC;s',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['1e-6', '1.6667e-8', '2.7778e-10', '1.1574e-11', '1.6534e-12', '8.2672e-13', '3.8052e-13', '3.171e-14', '1000', '1', '0.001']).put()
    milisecond_key = Unit(name='milisecond', type='time', abbreviation='ms',
        convert_units = ['second', 'minute', 'hour', 'day', 'week', 'fortnight', 'month', 'year', 'nanosecond', 'microsecond', 'milisecond'],
        convert_values = ['0.001', '1.6667e-5', '2.7778e-7', '1.1574e-8', '1.6534e-9', '8.2672e-10', '3.8052e-10', '3.171e-11', '1e+6', '1000', '1']).put()

    mass_key = UnitType(type='mass',
        units = ['gram', 'atomic-mass-unit', 'slug', 'solar-mass', 'kilogram']).put()
    gram_key = Unit(name='gram', type='mass', abbreviation='g',
        convert_units = ['gram', 'atomic-mass-unit', 'slug', 'solar-mass', 'kilogram'],
        convert_values = ['1.0', '6.022e+23', '6.85218e-5', '5e-34', '0.001']).put()
    atomic_mass_unit_key = Unit(name='atomic-mass-unit', type='mass', abbreviation='amu',
        convert_units = ['gram', 'atomic-mass-unit', 'slug', 'solar-mass', 'kilogram'],
        convert_values = ['1.66054e-24', '1.0', '1.13783e-28', '8.3027e-58', '1.66054e-27']).put()
    slug_key = Unit(name='slug', type='mass', abbreviation='sl',
        convert_units = ['gram', 'atomic-mass-unit', 'slug', 'solar-mass', 'kilogram'],
        convert_values = ['14593.9', '8.789e+27', '1.0', '7.296951468602e-30', '14.5939']).put()
    solar_mass_key = Unit(name='solar-mass', type='mass', abbreviation='M<sub>&#9737;</sub>',
        convert_units = ['gram', 'atomic-mass-unit', 'slug', 'solar-mass', 'kilogram'],
        convert_values = ['2e+33', '1.204427330335e+57', '1.370435317136e+29', '1.0', '2e+30']).put()
    kilogram_key = Unit(name='kilogram', type='mass', abbreviation='kg',
        convert_units = ['gram', 'atomic-mass-unit', 'slug', 'solar-mass', 'kilogram'],
        convert_values = ['1000', '6.022e+26', '0.0685218', '5e-31', '1']).put()

    temperature_key = UnitType(type='temperature',
        units = ['kelvin', 'celsius', 'fahrenheit']).put()
    kelvin_key = Unit(name='kelvin', type='temperature', abbreviation='K',
        convert_units = ['kelvin', 'celsius', 'fahrenheit'],
        convert_values = ['1.0', 'o', 'o']).put()
    celsius_key = Unit(name='celsius', type='temperature', abbreviation='&#8451;',
        convert_units = ['kelvin', 'celsius', 'fahrenheit'],
        convert_values = ['o', '1.0', 'o']).put()
    fahrenheit_key = Unit(name='fahrenheit', type='temperature', abbreviation='&#8457;',
        convert_units = ['kelvin', 'celsius', 'fahrenheit'],
        convert_values = ['o', 'o', '1.0']).put()

    volume_key = UnitType(type='volume',
        units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce']).put()
    meter_cubed_key = Unit(name='meter-cubed', type='volume', abbreviation='m<sup>3</sup>',
        convert_units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce'],
        convert_values = ['1.0', '35.3147', '1000', '264.172', '2113.38', '1056.69', '33814']).put()
    foot_cubed_key = Unit(name='foot-cubed', type='volume', abbreviation='ft<sup>3</sup>',
        convert_units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce'],
        convert_values = ['0.0283168', '1.0', '28.3168', '7.48052', '59.8442', '29.9221', '996.614']).put()
    liter_key = Unit(name='liter', type='volume', abbreviation='L',
        convert_units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce'],
        convert_values = ['0.001', '0.0353147', '1.0', '0.264172', '2.11338', '1.05669', '33.814']).put()
    us_gallon_key = Unit(name='gallon-US', type='volume', abbreviation='gal',
        convert_units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce'],
        convert_values = ['0.00378541', '0.133681', '3.78541', '1.0', '8', '4', '128']).put()
    us_pint_key = Unit(name='pint-US', type='volume', abbreviation='pt',
        convert_units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce'],
        convert_values = ['0.000473176', '0.0167101', '0.473176', '0.125', '1', '0.5', '16']).put()
    us_quart_key = Unit(name='quart-US', type='volume', abbreviation='qt',
        convert_units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce'],
        convert_values = ['0.000946353', '0.0334201', '0.946353', '0.25', '2', '1', '32']).put()
    fluid_ounce_key = Unit(name='fluid-ounce', type='volume', abbreviation='fl oz',
        convert_units = ['meter-cubed', 'foot-cubed', 'liter', 'gallon-US', 'pint-US', 'quart-US', 'fluid-ounce'],
        convert_values = ['2.9574e-5', '0.00104438', '0.0295735', '0.0078125', '0.0625', '0.03125', '1']).put()

    force_key = UnitType(type='force',
        units = ['newton', 'dyne', 'pound-force']).put()
    newton_key = Unit(name='newton', type='force', abbreviation='N',
        convert_units = ['newton', 'dyne', 'pound-force'],
        convert_values = ['1', '100000', '0.224809']).put()
    dyne_key = Unit(name='dyne', type='force', abbreviation='dyn',
        convert_units = ['newton', 'dyne', 'pound-force'],
        convert_values = ['1e-5', '1', '2.24809e-6']).put()
    pound_force_key = Unit(name='pound-force', type='force', abbreviation='lb<sub>f</sub>',
        convert_units = ['newton', 'dyne', 'pound-force'],
        convert_values = ['4.44822', '444822', '1']).put()

    energy_key = UnitType(type='energy',
        units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule']).put()
    joule_key = Unit(name='joule', type='energy', abbreviation='J',
        convert_units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule'],
        convert_values = ['1', '0.239006', '0.000947817', '6.242e+18', '2.7778e-7', '0.001', '1e-6']).put()
    calorie_key = Unit(name='calorie', type='energy', abbreviation='cal',
        convert_units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule'],
        convert_values = ['4.184', '1', '0.00396567', '2.611e+19', '1.1622e-6', '0.004184', '4.184e-6']).put()
    british_thermal_unit_key = Unit(name='british-thermal-unit', type='energy', abbreviation='BTU',
        convert_units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule'],
        convert_values = ['1055.06', '252.164', '1', '6.585e+21', '0.000293071', '1.05506', '0.00105506']).put()
    electron_volt_key = Unit(name='electron-volt', type='energy', abbreviation='eV',
        convert_units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule'],
        convert_values = ['1.6022e-19', '3.8293e-20', '1.5186e-22', '1', '4.4505e-26', '1.6022e-22', '1.6022e-25']).put()
    kilowatt_hour_key = Unit(name='kilowatt-hour', type='energy', abbreviation='kWh',
        convert_units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule'],
        convert_values = ['3.6e+6', '860421', '3412.14', '2.247e+25', '1', '3600', '3.6']).put()
    kilojoule_key = Unit(name='kilojoule', type='energy', abbreviation='kJ',
        convert_units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule'],
        convert_values = ['1000', '239.006', '0.947817', '6.242e+21', '0.000277778', '1', '0.001']).put()
    megajoule_key = Unit(name='megajoule', type='energy', abbreviation='MJ',
        convert_units = ['joule', 'calorie', 'british-thermal-unit', 'electron-volt', 'kilowatt-hour', 'kilojoule', 'megajoule'],
        convert_values = ['1e+6', '239006', '947.817', '6.242e+24', '0.277778', '1000', '1']).put()
