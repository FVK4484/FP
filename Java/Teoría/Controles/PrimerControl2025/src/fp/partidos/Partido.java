package fp.partidos;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Partido implements Comparable<Partido>{
	private LocalDate fechaPartido;
	private String equipoLocal;
	private String equipoVisitante;
	private Long numeroEspectadores;
	private Competicion competicion;
	private List<Resultado> resultadosParciales;
	
	public Partido(LocalDate fechaPartido, String equipoLocal, String equipoVisitante, Long numeroEspectadores,
			Competicion competicion, List<Resultado> resultadosParciales) {
		
		checkMinutosOrdenados(resultadosParciales);
		checkFechaPartido(fechaPartido);
		checkNumeroEspectadores(numeroEspectadores);
		this.fechaPartido = fechaPartido;
		this.equipoLocal = equipoLocal;
		this.equipoVisitante = equipoVisitante;
		this.numeroEspectadores = numeroEspectadores;
		this.competicion = competicion;
		this.resultadosParciales = new ArrayList<>(resultadosParciales);
		
	}

	public LocalDate getFechaPartido() {
		return fechaPartido;
	}

	public String getEquipoLocal() {
		return equipoLocal;
	}

	public String getEquipoVisitante() {
		return equipoVisitante;
	}

	public Long getNumeroEspectadores() {
		return numeroEspectadores;
	}

	public Competicion getCompeticion() {
		return competicion;
	}

	public List<Resultado> getResultadosParciales() {
		return new ArrayList<>(resultadosParciales);
	}
	
	public Integer getGolesLocal() {
		Integer goles = 0;
		if (resultadosParciales.isEmpty()) {
			throw new UnsupportedOperationException("La lista está vacía.");
		} else {
			goles = resultadosParciales.getLast().golesLocal();
		}
		return goles;
	}
	
	public Integer getGolesVisitante() {
		Integer goles = 0;
		if (resultadosParciales.isEmpty()) {
			throw new UnsupportedOperationException("La lista está vacía.");
		} else {
			goles = resultadosParciales.getLast().golesVisitante();
		}
		return goles;
	}

	public List<Integer> getMinutos() {
		List<Integer> minutos = new ArrayList<Integer>();
		if (resultadosParciales.isEmpty()) {
			throw new UnsupportedOperationException("La lista está vacía.");
		} else {
			for (Resultado r : resultadosParciales) {
				minutos.add(r.minuto());
			}
		}
		return minutos;
	}
	
	private void checkMinutosOrdenados(List<Resultado> resultadosParciales) {
		if (!minutosOrdenados(resultadosParciales)) {
			throw new IllegalArgumentException(
					"Los minutos de los resultados parciales deben estar ordenados de menor a mayor.");
		}
	}
	
	private void checkFechaPartido(LocalDate fechaPartido) {
		if (fechaPartido.isAfter(LocalDate.now())) {
			throw new IllegalArgumentException(
					"La fecha del partido no puede ser posterior a la fecha Actual.");
		}
	}
	
	private void checkNumeroEspectadores(Long numeroEspectadores) {
		if (numeroEspectadores < 0) {
			throw new IllegalArgumentException(
					"El número de espectadores es mayor o igual que 0.");
		}
	}
	
	public String toString() {
		return "Partido [fechaPartido=" + fechaPartido + ", equipoLocal=" + equipoLocal + ", equipoVisitante="
				+ equipoVisitante + ", numeroEspectadores=" + numeroEspectadores + ", competicion=" + competicion
				+ ", resultadosParciales=" + resultadosParciales + "]";
	}
	
	public int hashCode() {
		return Objects.hash(competicion, equipoLocal, equipoVisitante, fechaPartido, numeroEspectadores,
				resultadosParciales);
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Partido other = (Partido) obj;
		return competicion == other.competicion && Objects.equals(equipoLocal, other.equipoLocal)
				&& Objects.equals(equipoVisitante, other.equipoVisitante)
				&& Objects.equals(fechaPartido, other.fechaPartido)
				&& Objects.equals(numeroEspectadores, other.numeroEspectadores)
				&& Objects.equals(resultadosParciales, other.resultadosParciales);
	}

	public int compareTo(Partido p) {
		if (p == null) {
			throw new NullPointerException();
		} else {	
			Integer res = getFechaPartido().compareTo(p.getFechaPartido());
			if (res == 0) {
				res = getEquipoLocal().compareTo(p.getEquipoLocal());
				if (res == 0) {
					res = getEquipoVisitante().compareTo(p.getEquipoVisitante());
				}
			}
			return res;
		}
	}
	
	public Boolean minutosOrdenados(List<Resultado> resultadosParciales) {
		Integer res = 0;
		Boolean result = true;
		for (int i = 0; i < resultadosParciales.size() - 1; i++) {
			res = resultadosParciales.get(i + 1).minuto() - resultadosParciales.get(i).minuto();
			if (res < 0) {
				result = false;
				break;
			}
		}
		return result;
	}
	
}
