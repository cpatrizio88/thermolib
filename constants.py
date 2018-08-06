class constants:
   """ 
   A list of constants relevant to atmospheric science.

   References
   - - - - - -
   Emanuel appendix 2
   
   """
   Tc = 273.15; #0 deg C in Kelvin
   eps = 0.622;
   p0 = 1.e5;
   eps = 0.622;
   lv0 = 2.5104e6; # latent heat of vaporization of water J/kg
   lf = 0.3336e6; # latent heat of fusion of water J/kg
   Rv = 461.50; # J/kg/K
   Rd = 287.04; # J/kg/K
   cp = 1003.5 # Heat capacity of dry air (J/kg/K)
   cpv = 1870.; # Heat capacity of water vapor (J/kg/K)
   cl = 4190.;  # Heat capacity of liquid water (J/kg/K)
   cpd = 1005.7; # Heat capacity of dry air (J/kg/K)
   g = 9.81;      # m/s^2
   D = 2.36e-5;# Diffusivity m^2/s^1 
             # Note: fairly strong function of temperature
             #       and pressure -- this is at 100kPa, 10degC
   rhol = 1000.; #density of water (kg m^-3)
   rhoi = 916.7; #density of ice (kg m^-3)
   sig = 5.67e-8 #stefan Boltzmann contant
