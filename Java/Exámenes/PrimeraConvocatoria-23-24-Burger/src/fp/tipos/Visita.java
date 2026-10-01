package fp.tipos;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import fp.utiles.Checkers;

public class Visita implements Comparable<Visita>{
	private String email;
	private String ciudad;
	private String cp;
	private LocalDateTime entrada;
	private LocalDateTime salida;
	private Double temperatura;
	private List<Evaluacion> evaluaciones;
	
	public Visita(String email, String ciudad, String cp, LocalDateTime entrada, LocalDateTime salida,
			Double temperatura, List<Evaluacion> evaluaciones) {

		Checkers.check("El momento de salida debe ser posterior al momento de entrada.", 
				entrada.isBefore(salida));
		Checkers.check("El email debe contener el carácter ‘@’.",
				email.contains("@"));
		Checkers.check("La lista de evaluaciones debe contener al menos un elemento.",
				!evaluaciones.isEmpty());
		
		this.email = email;
		this.ciudad = ciudad;
		this.cp = cp;
		this.entrada = entrada;
		this.salida = salida;
		this.temperatura = temperatura;	
		this.evaluaciones = evaluaciones;
	}

	public LocalDateTime getSalida() {
		return salida;
	}

	public void setSalida(LocalDateTime salida) {
		Checkers.check("Visita::El día de entrada y de salida no son el mismo",
				salida.toLocalDate().equals(getEntrada().toLocalDate()));
		Checkers.check("Visita::Momentos de entrada y salida incorrectos",
				getEntrada().isBefore(salida));
		this.salida = salida;
	}

	public Double getTemperatura() {
		return temperatura;
	}

	public void setTemperatura(Double temperatura) {
		this.temperatura = temperatura;
	}

	public String getEmail() {
		return email;
	}

	public String getCiudad() {
		return ciudad;
	}

	public String getCp() {
		return cp;
	}

	public LocalDateTime getEntrada() {
		return entrada;
	}

	public List<Evaluacion> getEvaluaciones() {
		return new ArrayList<Evaluacion>(this.evaluaciones);
	}
	
	public Integer getNumEvaluaciones(){
		return getEvaluaciones().size();
		}
	
	public Double getPuntuacionMediaTotal() {
		Double suma = 0.0;
		for (Evaluacion ev: getEvaluaciones()) {
			suma += ev.puntuacion_final();
		}
		return suma / getEvaluaciones().size();
	}
	
	public TipoPaladar getPaladar() {
		TipoPaladar res = TipoPaladar.ALTO;
		if(getPuntuacionMediaTotal() >=  9) {
			res = TipoPaladar.BAJO;
		} else if(getPuntuacionMediaTotal() <  9 && getPuntuacionMediaTotal() > 6) {
			res = TipoPaladar.MEDIO;
		}
		return res;
	}
	
	public Duration getTiempoTranscurrido() {
		return Duration.between(getEntrada(), getSalida());
	}

	@Override
	public String toString() {
		return "Visita [email=" + email + ", ciudad=" + ciudad + ", cp=" + cp + ", entrada=" + entrada + ", salida="
				+ salida + ", temperatura=" + temperatura + ", evaluaciones=" + evaluaciones + "]";
	}

	@Override
	public int hashCode() {
		return Objects.hash(email, entrada, salida);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Visita other = (Visita) obj;
		return Objects.equals(email, other.email) && Objects.equals(entrada, other.entrada)
				&& Objects.equals(salida, other.salida);
	}

	public int compareTo(Visita o) {
		int res = getEntrada().compareTo(o.getEntrada())
				+ getSalida().compareTo(o.getSalida());
			if(res == 0) {
				res = getEmail().compareTo(o.getEmail());
				}
		return res;
	}
}