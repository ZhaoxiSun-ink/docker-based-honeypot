FROM httpd:latest
COPY index.html /usr/local/apache2/htdocs
# Enable necessary modules
RUN sed -i 's/#LoadModule ldap_module modules\/mod_ldap.so/LoadModule ldap_module modules\/mod_ldap.so/' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's/#LoadModule authnz_ldap_module modules\/mod_authnz_ldap.so/LoadModule authnz_ldap_module modules\/mod_authnz_ldap.so/' /usr/local/apache2/conf/httpd.conf

# Copy custom configuration
COPY ldap.conf /usr/local/apache2/conf/extra/

# Include the custom configuration in httpd.conf
#RUN echo "Include conf/extra/ldap.conf" >> /usr/local/apache2/conf/httpd.conf
EXPOSE 80
