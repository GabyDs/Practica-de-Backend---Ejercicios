# Practica-de-Backend---Ejercicios

## Primer Ejercicio : Sistema de autenticación y gestión de usuarios (rolesapp)

Este proyecto busca implementar un sistema de autenticación y gestión de usuarios con los siguientes requisitos:

1. **Registro y login de usuarios:**
    * Los usuarios deben poder registrarse y acceder a la aplicación mediante un sistema de login.
    * Si un usuario intenta registrarse estando ya autenticado, el sistema debe mostrar un mensaje informándole que ya está logueado.
2. **Roles de usuario:**
    * **Usuarios normales:** Pueden registrarse y acceder a vistas específicas, como contenido o funcionalidades limitadas para usuarios registrados.
    * **Administradores:** Además de acceder a las vistas de usuarios normales, deben tener permisos adicionales para:
      * Crear nuevos usuarios (normales o administradores).
      * Editar o eliminar usuarios existentes.
      * Administrar contenido futuro que se añada al proyecto.
3. **Flujo de primer administrador:**
    * El primer usuario con rol de administrador se creará manualmente mediante comandos para garantizar una configuración inicial segura.

Este ejercicio sirve como base para aprender a implementar flujos de autenticación, gestión de permisos y vistas personalizadas según el rol del usuario, utilizando Django.