package fp.tipos;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Objects;

public class Persona implements Comparable <Persona>{
	private String dni;
	private String apellidos;
	private String nombre;
	private LocalDate fechaNacimiento;
	private String email;
	
	public Persona(String dni, String apellidos, String nombre, LocalDate fechaNacimiento, String email) {
		checkDni(dni);
		checkEmail(email);
		this.dni = dni;
		this.apellidos = apellidos;
		this.nombre = nombre;
		this.fechaNacimiento = fechaNacimiento;
		this.email = email;
	}

	public Persona(String dni, String apellidos, String nombre, LocalDate fechaNacimiento) {
		this(dni, apellidos, nombre, fechaNacimiento, "");
	}

	public String getDni() {
		return dni;
	}

	public void setDni(String dni) {
		checkDni(dni);
		this.dni = dni;
	}

	public String getApellidos() {
		return apellidos;
	}

	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}

	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		checkEmail(email);
		this.email = email;
	}
	
	public Integer getEdad() {
		return fechaNacimiento.until(LocalDate.now()).getYears();
	}
	
	private void checkDni(String dni) {
		if (dni.length() != 9 || !caracteresDni(dni) == true){
			throw new IllegalArgumentException
			("El DNI de una persona está formado por 8 dígitos y una letra.");
		}
	}

	private Boolean caracteresDni(String dni) {
		Boolean res = true;
		for (int i = 0; i < dni.length() - 1; i++) {
			if (!Character.isDigit(dni.charAt(i))) {
				res = false;
				break;
			}
		} for (int i = 8; i < dni.length(); i++) {
			if (!Character.isLetter(dni.charAt(i))) {
				res = false;
				break;
			}
		}
		return res;
	}
	
	private void checkEmail(String email) {
		if (!(email.contains("@")) || email.isEmpty()) {
			throw new IllegalArgumentException
			("El email debe contener el carácter '@' o estar vacía.");
		}
	}

	public String toString() {
		return dni + " - " + apellidos + ", " + nombre + " - "
				+ fechaNacimiento.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));
	}

	public int hashCode() {
		return Objects.hash(apellidos, dni, nombre);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Persona other = (Persona) obj;
		return Objects.equals(apellidos, other.apellidos) && Objects.equals(dni, other.dni)
				&& Objects.equals(nombre, other.nombre);
	}

	public int compareTo(Persona p) {
		Integer res = getApellidos().compareTo(p.getApellidos());
		if (res == 0) {
			res = getNombre().compareTo(p.getNombre());
			if (res == 0) {
				res = getDni().compareTo(p.getDni());
			}
		}
		return res;
	}
	
}
